# HCG Web

HCG（Hybrid Code Graph）是一个运行在浏览器中的代码图分析工具。它可以针对代码生成并展示 CFG、AST 和 PDG，并提供代码修复、代码图问答及 AI 辅助调整图等功能。

## 直接使用（推荐）

打开在线版本：

**https://bankzhy.github.io/hcg/**

在线版本无需安装 Flutter、Node.js、Python，也无需下载仓库。建议使用最新版 Chrome 或 Edge。

> HCG 客户端本身可以直接运行，但 AI 功能仍需要一个可访问的 LLM 服务，例如本机 Ollama 或兼容 OpenAI API 的远程服务。

## 安装到电脑

HCG 支持安装为 Web App。安装后可以像普通桌面应用一样，从系统应用列表或桌面图标启动。

### Chrome / Edge

1. 打开 [HCG 在线版本](https://bankzhy.github.io/hcg/)。
2. 点击地址栏右侧的“安装”图标。
3. 如果没有显示该图标，请打开浏览器菜单，选择“安装 HCG”或“应用 → 安装此网站为应用”。
4. 安装完成后，从系统应用列表启动 HCG。

这种方式不需要安装开发环境，应用更新后浏览器会自动获取新版本。

## 首次配置

启动后进入 **Settings** 页面，配置模型服务：

- **本地 Ollama**：通常使用 `http://localhost:11434/v1`。
- **远程模型 API**：填写兼容 OpenAI API 的地址、模型名称和 API Key。
- 配置保存在当前浏览器的本地存储中，不会提交到本仓库。

使用远程 API 时，该服务必须允许浏览器跨域访问（CORS）。请勿在公共或不受信任的电脑上保存私人 API Key。

## 下载仓库文件

如需下载已经编译好的 Web 文件：

1. 打开本仓库主页。
2. 点击 **Code → Download ZIP**。
3. 解压下载的 ZIP 文件。

本仓库保存的是已经编译好的 Web 发布文件，不是 Flutter 源代码。不要直接双击 `index.html`：浏览器的 `file://` 安全限制会导致应用无法正常加载。普通用户应使用上面的在线版本或安装 Web App。

如果需要部署到自己的静态 Web 服务器，请通过 HTTP/HTTPS 提供这些文件，并保留 `/hcg/` 访问路径；当前构建的基础路径为 `/hcg/`。

## 浏览器支持

- 推荐：最新版 Chrome、Edge
- Firefox、Safari：基本页面可以使用，但安装 Web App 和本地模型访问能力可能受到浏览器限制

## 评价数据集

用于开发者评价的代码文件位于 [`evaluation_dataset`](evaluation_dataset/)。
该目录包含 `developer_01` 至 `developer_10` 十个文件夹，每位评价者使用分配给自己的文件夹，并在 HCG 的 **Files → Import Folder** 中一次性导入。

每个文件夹包含 60 个样本：Java、Python、JavaScript 各 20 个。请勿查看或使用其他评价者的文件夹。

## English quick start

Open **https://bankzhy.github.io/hcg/** in the latest Chrome or Edge. No Flutter, Node.js, or Python installation is required. To install it as a desktop-like app, use the install icon in the browser address bar. AI features require a reachable Ollama or OpenAI-compatible API service.
