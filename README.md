# HCG Web

HCG (Hybrid Code Graph) is a browser-based code analysis tool that combines lightweight static analysis with large language models. It generates and visualizes CFG, AST, and PDG graphs, and provides code repair, code-graph queries, highlighted code-to-graph mapping, manual graph editing, and AI-assisted graph modification.

## Demo

- [Watch the HCG demonstration video](https://youtu.be/Oi5JmsrKvLU)
- [Open the online version](https://bankzhy.github.io/hcg/)

## Interface Languages

HCG provides its user interface in three languages:

- English (default)
- Simplified Chinese (简体中文)
- Japanese (日本語)

Users can switch the interface language at any time with the **Language** selector on the **Settings** page. The selected language is saved in the browser and restored the next time HCG is opened.

## LLM Connection Options

HCG runs entirely in the browser, but its AI features require an accessible LLM service.

### Using a local LLM with Ollama

When you want to use a local LLM, install and run [Ollama](https://ollama.com/) on your computer. Downloading the HCG repository is not mandatory: you can first use the [online HCG application](https://bankzhy.github.io/hcg/) and connect it to Ollama.

1. Install and start Ollama.
2. Download a model, for example:

   ```bash
   ollama pull qwen3:4b
   ```

3. Open the [online HCG application](https://bankzhy.github.io/hcg/).
4. On the HCG **Settings** page, enter:

   - API base URL: `http://localhost:11434/v1`
   - Model: the Ollama model name you downloaded
   - API key: leave empty unless your Ollama setup requires one

Browser security settings may prevent a public HTTPS page from connecting to a service on `localhost`. If the online version cannot reach Ollama, run HCG locally as an optional fallback:

   ```bash
   git clone https://github.com/Bankzhy/hcg.git
   python3 -m http.server 8080
   ```

Then open [http://localhost:8080/hcg/](http://localhost:8080/hcg/) and use the same Ollama settings shown above. Run the server command from the directory that contains the cloned `hcg` folder.

The repository contains the compiled Web application, so Flutter, Node.js, and other development dependencies are not required. Do not open `index.html` directly with `file://`; HCG must be served over HTTP or HTTPS.

### Remote use: enter an API directly

When using a remote LLM service, local Ollama is not required. Open the [online HCG application](https://bankzhy.github.io/hcg/) and enter the following information on the **Settings** page:

- An OpenAI-compatible API base URL
- The model name
- The API key, if required

The remote service must allow browser requests through CORS and should provide an HTTPS endpoint. Settings are stored only in the current browser's local storage. Do not save a private API key on a public or untrusted computer.

## Install as a Web App

In a recent version of Chrome or Edge:

1. Open the [HCG online version](https://bankzhy.github.io/hcg/).
2. Select the install icon in the address bar.
3. If the icon is not visible, open the browser menu and select **Install HCG** or **Apps → Install this site as an app**.
4. Start HCG from the system application list after installation.

This installs the interface as a desktop-like Web App. AI features still require either a reachable local Ollama service or a remote API.

## Browser Support

- Recommended: the latest Chrome or Edge
- Firefox and Safari: the basic interface may work, but Web App installation and local-model access can be more restricted

## Evaluation Dataset

The code samples for the developer evaluation are located in [`evaluation_dataset`](evaluation_dataset/). The directory contains `developer_01` through `developer_10`, with one assigned folder for each evaluator.

Each folder contains 60 samples: 20 Java, 20 Python, and 20 JavaScript files. Import the assigned folder in HCG through **Files → Import Folder**. Evaluators should use only their assigned folder.
