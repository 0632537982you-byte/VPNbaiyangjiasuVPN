# 白羊加速
白羊加速（Aries VPN）是一款专为追求极致速度用户打造的安全、稳定、高速的VPN/梯子，翻墙工具。我们不是复杂的机场订阅，而是提供简单易用的一键式翻墙软件。无论你是需要观看Netflix/YouTube 8K视频，还是保护在线隐私，白羊加速都能满足你。
# Clash to v2rayN Converter (GUI Version)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

一个简单、轻量级的桌面工具，用于将 Clash 订阅链接（YAML 格式）转换为 v2rayN/v2rayNG 等软件支持的 Base64 订阅链接。

## ✨ 功能特点

* **图形化界面**：无需通过命令行操作，所见即所得。
* **多协议支持**：支持解析 `VMess`、`Shadowsocks (SS)` 和 `Trojan` 节点。
* **自动转码**：自动处理 JSON 封装与 Base64 编码。
* **便捷导出**：支持一键复制结果到剪贴板或导出为 `.txt` 文件。

## 🛠️ 依赖环境

使用前请确保已安装 Python 3.x，并安装以下依赖库：

```bash
pip install pyyaml requests
```

## 🚀 快速开始

1.  克隆仓库或下载源码：
    ```bash
    git clone [https://github.com/your-username/clash2v2ray-gui.git](https://github.com/your-username/clash2v2ray-gui.git)
    cd clash2v2ray-gui
    ```

2.  运行程序：
    ```bash
    python main.py
    ```

3.  **使用步骤**：
    * 在输入框中粘贴你的 Clash 订阅链接。
    * 点击 **"开始转换"**。
    * 查看日志确认转换成功后，点击 **"复制结果"**。
    * 打开 v2rayN -> 订阅 -> 添加订阅 URL -> 粘贴即可。

## 📦 打包为可执行文件 (.exe)

如果你想在没有安装 Python 的电脑上运行，可以使用 `pyinstaller` 打包：

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```
打包完成后，`dist` 目录下会生成 `main.exe`。

## 📝 注意事项

* 本工具仅用于不同软件格式间的配置转换，**不提供**任何代理节点。
* 目前仅支持 Clash 配置文件中的 `proxies` 字段解析。
* 不支持 Hysteria / VLESS 等较新协议（待更新）。

## 📄 开源协议

MIT License
