<div align="center">

Clash转v2ray工具 (GUI桌面版) & 白羊加速

🚀 免费高速VPN推荐 | 稳定梯子 | 翻墙工具 | 4K/8K视频秒开 | 科学上网首选

</div>

📖 项目简介

这是一个简单、轻量级的 Python 桌面工具 (GUI)，专为解决格式不兼容问题而生。它可以将 Clash 订阅链接（YAML 格式）一键转换为 v2rayN / v2rayNG / Shadowrocket 等软件支持的 Base64 订阅链接。

本项目由 白羊加速 赞助支持。 如果你需要稳定、高速的节点源，请继续阅读下文。

🚀 白羊加速 - 免费高速VPN推荐

白羊加速（Aries VPN）是一款专为追求极致速度用户打造的安全、稳定、高速的 | VPN | 梯子工具。我们摒弃复杂的机场订阅配置，提供简单易用的一键式翻墙软件。

无论你是需要观看 Netflix / YouTube 8K 视频，还是使用 ChatGPT / Gemini / Midjourney，白羊加速都能提供如同内网般的流畅体验。

🌟 核心亮点：全平台支持 | 不限速 | 无限制流量 | 晚高峰稳定不掉线 | 解锁流媒体

⚡ 为什么选择白羊加速？

白羊加速致力于提供最佳的科学上网体验，彻底解决传统 VPN 经常断连、速度慢的痛点：

极速体验：拥有并部署 IPLC/IEPL 专线节点，8K 视频秒开，拒绝缓冲等待。

隐私安全：采用最新军用级加密技术，隐藏真实 IP，保护您的在线隐私和数据安全。

灵活套餐：支持包月无限流量及无限期流量套餐，丰俭由人。

简单易用：非传统机场模式，无需学习复杂配置，下载软件即可一键连接。

免费试用：每日签到领取免费时长，新用户注册更有好礼相送。

📥 官网下载与注册

点击下方链接立即注册，开启自由网络之旅：

👉 点击访问白羊加速官网 (注册领免费时长)

(注：如果网站无法打开，请尝试切换网络环境或 CDN 节点。部分地区如新疆、福建等可能存在访问限制)

📱 iOS / 苹果手机用户指南

获取软件：由于 iOS 政策限制，你需要使用美区 Apple ID 登录 App Store 下载 Shadowrocket (小火箭)。

导入节点：在 白羊加速官网 注册并获取 订阅链接。

一键连接：将订阅链接导入 Shadowrocket 即可开始使用。

🎉 最新福利活动 (限时)

1️⃣ 拉新送时长 - 上不封顶！

邀请好友注册，双方均可获赠时长：

邀请 10 位用户：送 1 个月 VIP

邀请 27 位用户：送 1 个季度 VIP

参与方式：邀请达标后，联系客服或提交工单，立即开通对应时长！

2️⃣ 限时免费 & 补偿福利

为回馈新老用户，官网近期大放送：

BUG 补偿：随机赠送 7-60 天 VIP 使用时长。

每日福利：每日签到即可抽取随机免费 VPN 时长或额外流量。

新人礼品码：

当前可用兑换码：BYAE7A9799B9F6

使用方法：下载应用后 -> 右上角点击兑换。

(提示：该礼品码 24 小时内仅限使用一次，手慢无！)

🛠️ 转换工具使用指南

如果你手头已经有 Clash 订阅链接，但想在 v2rayN 中使用，请使用本项目提供的代码。

✨ 功能特点

🖥️ 图形化界面：无需命令行，小白也能轻松操作。

🔄 多协议支持：支持解析 VMess、Shadowsocks (SS) 和 Trojan 节点。

⚡ 自动转码：自动处理 JSON 封装与 Base64 编码。

📂 便捷导出：支持一键复制结果到剪贴板或导出为 .txt 文件。

📦 依赖环境

使用前请确保已安装 Python 3.x，并安装以下依赖库：

pip install pyyaml requests


🏃‍♂️ 快速开始

克隆仓库或下载源码：

git clone [https://github.com/your-username/clash2v2ray-gui.git](https://github.com/your-username/clash2v2ray-gui.git)
cd clash2v2ray-gui


运行程序：

python main.py


操作步骤：

在输入框中粘贴你的 Clash 订阅链接。

点击 "开始转换"。

查看日志确认转换成功后，点击 "复制结果"。

打开 v2rayN -> 订阅 -> 添加订阅 URL -> 粘贴即可。

📦 打包为可执行文件 (.exe)

如果你想在没有 Python 的电脑上运行，可以使用 pyinstaller 打包：

pip install pyinstaller
pyinstaller --onefile --windowed main.py


打包完成后，dist 目录下会生成 main.exe。

📄 开源协议

MIT License

<!--
SEO Keywords / 搜索引擎关键词优化:
clash转v2ray, vmess转换, 科学上网, 翻墙VPN, 免费梯子, 白羊加速, Aries VPN, 免费SSR, Trojan节点, 电脑VPN, 安卓VPN, iOS翻墙, 8K秒开, ChatGPT梯子, Python脚本, 免费VPN, 稳定机场
-->
