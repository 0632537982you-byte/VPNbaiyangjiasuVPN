# 🛠️ Clash转v2ray工具 (GUI版) & 🚀 免费高速VPN推荐

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

### 🏆 特别推荐：白羊加速 (Aries VPN)
> **还在寻找稳定的翻墙工具？**
> 白羊加速提供 IPLC/IEPL 专线，拒绝晚高峰卡顿。

* **🚀 极速体验**：油管 4K/8K 视频秒开，无缓冲。
* **🔓 全能解锁**：完美支持 ChatGPT, Gemini, Midjourney, Netflix, Disney+。
* **📱 全平台**：支持 Windows, Mac, Android, iOS (Shadowrocket)。
* **🎁 免费试用**：注册即送时长，每日签到领流量。

👉 **[立即点击注册：白羊加速官网 (含最新优惠)](https://baiyangjiasu.com/register?invite=VD7GZSba接)**
*(新人福利码：`BYAE7A9799B9F6` | 下载APP -> 右上角兑换)*

---

## 📖 项目简介

一个简单、轻量级的桌面工具，用于将 Clash 订阅链接（YAML 格式）转换为 v2rayN / v2rayNG 等软件支持的 Base64 订阅链接。

## ✨ 功能特点

* **图形化界面**：无需通过命令行操作，所见即所得。
* **多协议支持**：支持解析 `VMess`、`Shadowsocks (SS)` 和 `Trojan` 节点。
* **自动转码**：自动处理 JSON 封装与 Base64 编码。
* **便捷导出**：支持一键复制结果到剪贴板或导出为 `.txt` 文件。

## 🛠️ 依赖环境

使用前请确保已安装 **Python 3.x**，并安装以下依赖库：

```bash
pip install pyyaml requests
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
<details> 

🔥 热门工具与客户端
Clash, Clash for Windows, Clash Verge, Clash Meta, Clash Nyanpasu, v2rayN, v2rayNG, Shadowrocket, 小火箭, Quantumult X, Loon, Surge, Stash, Egern, Pharos, Sing-box, Hysteria, Tuic, Juicity, Nekobox.

🚀 (VPN Recommendations)
ExpressVPN, NordVPN, Surfshark, VyprVPN, ProtonVPN, PureVPN, Astrill VPN, Private Internet Access (PIA). 国内热门：熊猫加速器 (PandaVPN), 老王VPN, 蚂蚁加速器, 蓝灯 (Lantern), 佛跳墙VPN, 旋风加速器, 极光加速器, 狗急加速器, 快连VPN, Let's VPN.

科学上网, 翻墙, 梯子, 免费VPN, 免费梯子, 电脑VPN, 安卓VPN, iOS翻墙, 苹果VPN, 机场推荐, 稳定机场, 翻墙软件, 中国VPN, VPN for China, 翻墙回国, 免费节点, 订阅链接, 机场测速, 机场订阅转换.


ChatGPT梯子, 解锁Netflix, 观看YouTube 4K, Midjourney绘图, 稳定的梯子, 游戏加速器, 外网加速器, GitHub加速, 谷歌学术, 跨境电商, TikTok直播, 奈飞解锁.

</details>
MIT License
