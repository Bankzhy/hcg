# HCG Web

HCG（Hybrid Code Graph）是一个本地优先的代码图分析客户端，可生成和展示 CFG、AST 与 PDG，并提供代码修复、代码图问答及 AI 辅助图编辑功能。

## 下载并在本地运行（推荐）

本仓库已包含编译后的 Web 客户端，不需要安装 Flutter 或 Node.js。

1. 在仓库主页点击 **Code → Download ZIP**。
2. 解压 ZIP。
3. 在解压后的目录运行启动脚本。

macOS / Linux：

```bash
bash start.sh
```

Windows：

```bat
start.bat
```

启动器会自动打开：

```text
http://127.0.0.1:4173/hcg/
```

若 4173 端口已被占用，会自动使用后续可用端口。按 `Ctrl+C` 停止 HCG。

运行时只需要 Python 3，不需要 Flutter。可先用以下命令确认：

```bash
python3 --version
```

Windows 可使用：

```bat
py -3 --version
```

## 连接本地 Ollama

1. 安装并启动 [Ollama](https://ollama.com/download)。
2. 下载需要的模型，例如：

```bash
ollama pull qwen3:4b
```

3. 在 HCG 的 **Settings** 页面填写：

- Base URL：`http://127.0.0.1:11434/v1`
- API Key：`ollama`
- Model：`ollama list` 中显示的模型名称

4. 点击 **Save** 和 **Test Connection**。

HCG 与 Ollama 都通过 `127.0.0.1` 运行，因此一般不需要额外配置 `OLLAMA_ORIGINS`。

## 使用评价数据

在分析页面左侧的 **Files** 标签中点击 **Import Folder**，选择研究者分配的 `developerXX` 文件夹。代码只在当前浏览器和本机 Ollama 中处理。

## 注意事项

- 不要直接双击 `index.html`；浏览器的 `file://` 限制会导致 Flutter Web 无法正常加载。
- 推荐最新版 Chrome 或 Edge。
- 如果无法连接 Ollama，请确认 `http://127.0.0.1:11434/api/tags` 可以访问。
- 本地配置保存在当前浏览器的本地存储中。

## English quick start

Download the repository ZIP, extract it, and run `bash start.sh` on macOS/Linux or `start.bat` on Windows. Open `http://127.0.0.1:4173/hcg/` and configure Ollama with `http://127.0.0.1:11434/v1`. Flutter and Node.js are not required; Python 3 is required only for the local launcher.
