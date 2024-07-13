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


### Additional Notes

These helpers are not meant to be end-all solutions. They are provided as-is to help new and curious Ollama users get past some of the challenges I experienced during my journey using Ollama and local LLMs. I hope you find these helpers useful in yours.

#### Getting Started with Local LLMs

If you are new to local LLMs and unsure of your workstation's capabilities, start by downloading one of the smaller models. I like using `tinydolphin:1.1b-v2.8-q5_K_M`—response times seem to be quicker than many other models, something I find valuable when just trying to see if something is working. Once you are sure your setup is functioning as expected, then start exerimenting with larger more capable models.

#### Handling Model Memory Issues

When using the chat interface, if you switch models and encounter an error like "model is too large for this system," it may be due to the previous model still residing in memory. You can check this by running:

```sh
ollama ps
```

If you are using default settings, the unused model should unload itself from memory after a few minutes. Once it clears you can try the new model again, if you still get the error, that model may actually be too large for you to run. (check Ollama docs for details).


Good Luck and enjoy the journey!
