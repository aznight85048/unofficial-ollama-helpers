# Unofficial Ollama Helpers
**Disclaimer: These tools are unofficial and are not sponsored or endorsed by Ollama. They are developed in conjunction with AI to assist with using `ollama serve`.**

This repository contains various helpers and tools for working with `ollama serve`.

## Contents

- **helpers/**: Contains helper scripts and utilities (no frameworks--no 3rd party code). 
  - `availability_checker.html`: An HTML/JavaScript utility to check the availability of the `ollama serve` and proxy ports.
  - `ollama_proxy.py`: A base Python proxy server to bypass CORS issues. 

- **chat-interface/**: A browser-based chat interface using HTML and vanilla JavaScript.

## Getting Started

### Helpers

#### availability_checker.html
Open `availability_checker.html` in a web browser to check the availability of the `ollama serve` and proxy ports.


#### ollama_proxy.py
To run the proxy server, execute the following command:
```bash
python ollama_proxy.py
```

### Chat Interface
Open `api-chat-interface.html` in a web browser to use the simple browser-based chat interface.


## Related Projects

For a more advanced chat interface, check out the [promptGenAI](https://github.com/aznight85048/promptgenai) repository.
