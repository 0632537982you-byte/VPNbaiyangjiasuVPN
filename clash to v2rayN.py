import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yaml
import json
import base64
import requests
import urllib.parse
import threading

# --- 核心转换逻辑 (保持不变) ---
def safe_base64_encode(s):
    if isinstance(s, str):
        s = s.encode('utf-8')
    return base64.b64encode(s).decode('utf-8')

def create_vmess_uri(proxy):
    vmess_config = {
        "v": "2",
        "ps": proxy.get("name", "VMess Node"),
        "add": proxy.get("server", ""),
        "port": str(proxy.get("port", 80)),
        "id": proxy.get("uuid", ""),
        "aid": str(proxy.get("alterId", 0)),
        "scy": proxy.get("cipher", "auto"),
        "net": proxy.get("network", "tcp"),
        "type": "none",
        "host": "",
        "path": "",
        "tls": ""
    }
    if proxy.get("network") == "ws":
        ws_opts = proxy.get("ws-opts", {})
        vmess_config["path"] = ws_opts.get("path", "/")
        vmess_config["host"] = ws_opts.get("headers", {}).get("Host", "")
    if proxy.get("tls"):
        vmess_config["tls"] = "tls"
    return "vmess://" + safe_base64_encode(json.dumps(vmess_config))

def create_ss_uri(proxy):
    user_info = f"{proxy.get('cipher', '')}:{proxy.get('password', '')}"
    name = urllib.parse.quote(proxy.get("name", "SS Node"))
    return f"ss://{safe_base64_encode(user_info)}@{proxy.get('server')}:{proxy.get('port')}#{name}"

def create_trojan_uri(proxy):
    uri = f"trojan://{proxy.get('password')}@{proxy.get('server')}:{proxy.get('port')}"
    if proxy.get("sni"):
        uri += f"?sni={proxy.get('sni')}"
    return uri + f"#{urllib.parse.quote(proxy.get('name', 'Trojan'))}"

# --- GUI 界面类 ---
class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clash 2 v2rayN 转换器")
        self.root.geometry("600x450")
        
        # 变量
        self.url_var = tk.StringVar()
        self.result_data = "" # 存储转换结果

        self.create_widgets()

    def create_widgets(self):
        # 1. 输入区域
        input_frame = ttk.LabelFrame(self.root, text="订阅设置", padding=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(input_frame, text="Clash 订阅链接:").pack(side="left")
        entry = ttk.Entry(input_frame, textvariable=self.url_var, width=50)
        entry.pack(side="left", padx=5, fill="x", expand=True)

        # 2. 按钮区域
        btn_frame = ttk.Frame(self.root, padding=5)
        btn_frame.pack(fill="x", padx=10)
        
        convert_btn = ttk.Button(btn_frame, text="开始转换", command=self.start_conversion)
        convert_btn.pack(side="left", padx=5)
        
        save_btn = ttk.Button(btn_frame, text="保存结果到文件", command=self.save_file)
        save_btn.pack(side="left", padx=5)

        copy_btn = ttk.Button(btn_frame, text="复制结果到剪贴板", command=self.copy_to_clipboard)
        copy_btn.pack(side="left", padx=5)

        # 3. 日志/输出区域
        log_frame = ttk.LabelFrame(self.root, text="转换日志 & 预览", padding=10)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_text = tk.Text(log_frame, height=15, state="disabled", font=("Consolas", 9))
        self.log_text.pack(fill="both", expand=True)

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.config(state="disabled")

    def start_conversion(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("提示", "请输入 Clash 订阅链接")
            return
        
        self.log_text.config(state="normal")
        self.log_text.delete(1.0, "end") # 清空日志
        self.log_text.config(state="disabled")
        
        # 使用多线程防止界面卡死
        threading.Thread(target=self.run_conversion, args=(url,), daemon=True).start()

    def run_conversion(self, url):
        self.log(f"正在请求: {url} ...")
        try:
            headers = {'User-Agent': 'Clash/1.0'}
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            
            self.log("下载成功，正在解析 YAML...")
            data = yaml.safe_load(resp.text)
            proxies = data.get("proxies", [])
            
            links = []
            for p in proxies:
                ptype = p.get("type")
                link = ""
                if ptype == "vmess": link = create_vmess_uri(p)
                elif ptype == "ss": link = create_ss_uri(p)
                elif ptype == "trojan": link = create_trojan_uri(p)
                
                if link:
                    links.append(link)
                    self.log(f"[成功] {p.get('name')}")
            
            if not links:
                self.log("未找到支持的节点类型 (VMess/SS/Trojan)。")
                return

            raw_text = "\n".join(links)
            self.result_data = safe_base64_encode(raw_text)
            
            self.log("-" * 30)
            self.log(f"转换完成！共 {len(links)} 个节点。")
            self.log("你可以直接点击'复制'或'保存'按钮。")
            
        except Exception as e:
            self.log(f"[错误] {str(e)}")

    def save_file(self):
        if not self.result_data:
            messagebox.showinfo("提示", "请先进行转换。")
            return
        filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(self.result_data)
            messagebox.showinfo("成功", "文件已保存。")

    def copy_to_clipboard(self):
        if not self.result_data:
            messagebox.showinfo("提示", "请先进行转换。")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(self.result_data)
        messagebox.showinfo("成功", "已复制订阅内容到剪贴板。")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
