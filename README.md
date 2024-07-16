# Unofficial Ollama Helpers

**Disclaimer**: These tools are unofficial and are not sponsored or endorsed by Ollama. They are developed in conjunction with AI to assist with using `ollama serve`.

This repository contains various helpers and tools for working with `ollama serve`.

## Contents

- **Main Repository Files**:
  - `README.md`: This document, providing an overview and instructions.
  - `LICENSE`: The licensing information for the repository.
  - `.gitignore`: Specifies files to be ignored by Git.
  - `availability_checker.html`: An HTML/JavaScript utility to check the availability of the `ollama serve` and proxy ports.
  - `ollama_proxy.py`: A base Python proxy server to bypass CORS issues.
  - `api-chat-interface.html`: A browser-based chat interface using HTML and vanilla JavaScript.

## Getting Started

### availability_checker.html
Use this utility to check if the `ollama serve` and proxy ports are available. 

**Steps:**
1. Open `availability_checker.html` in a web browser.
2. Follow the on-screen instructions to check port availability.

### ollama_proxy.py
This Python script serves as a proxy server to bypass CORS issues when accessing the Ollama Serve API from a browser.

**Steps:**
1. Ensure Python is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `ollama_proxy.py`.
4. Run the following command:
   ```bash
   python ollama_proxy.py
   ```
5. Keep the terminal open while you use the chat interface or any other browser-based utility.

### api-chat-interface.html
A simple browser-based chat interface for interacting with the Ollama Serve API.

**Steps:**
1. Open `api-chat-interface.html` in a web browser.
2. Start chatting with the model.

## Detailed Step-by-Step Guide

If you are new to GitHub, local LLMs, or need more detailed instructions, please refer to the [Step-by-Step Guide](docs/step_by_step_guide.md).

## Related Projects
For a more advanced chat interface, check out the [promptGenAI](https://github.com/aznight85048/promptgenai) repository.

## Additional Notes

These helpers are not meant to be end-all solutions. They are provided as-is to help new and curious Ollama users get past some of the challenges I experienced during my journey using Ollama and local LLMs. I hope you find these helpers useful on your journey.

### Getting Started with Local LLMs

If you are new to local LLMs and unsure of your workstation's capabilities, start by downloading one of the smaller models. I recommend using `tinydolphin:1.1b-v2.8-q5_K_M`—response times seem to be quicker than many other models, something I find valuable when just trying to see if something is working. Once you are sure your setup is functioning as expected, start experimenting with larger, more capable models.

### Handling Model Memory Issues

When using the chat interface, if you switch models and encounter an error like "model is too large for this system," it may be due to the previous model still residing in memory. You can check this by running:
```sh
ollama ps
```
If you are using default settings, the unused model should unload itself from memory after a few minutes. Once it clears, you can try the new model again. If you still get the error, that model may actually be too large for you to run (check Ollama docs for details).

Good Luck and enjoy the journey!

---

## Step-by-Step Guide

### Prerequisites
1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Ollama Serve API**: Follow the instructions in the Ollama documentation to install and configure the Ollama Serve API.

### Setting Up Helpers

#### Setting Up the Proxy Server
1. **Download the Script**: Clone or download the repository from GitHub.
2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing `ollama_proxy.py`.
   - Run the command:
     ```bash
     python ollama_proxy.py
     ```
   - The proxy server will start, and you should see output indicating that it is running.

#### Using the Availability Checker
1. **Open the File**: Double-click `availability_checker.html` to open it in your default web browser.
2. **Check Ports**: Follow the on-screen instructions to check the availability of the `ollama serve` and proxy ports.

#### Using the Chat Interface
1. **Open the Interface**: Double-click `api-chat-interface.html` to open it in your default web browser.
2. **Start Chatting**: Use the interface to interact with the Ollama Serve API.

---

## FAQ

**Q: What is `ollama serve`?**
A: `ollama serve` is an API for serving machine learning models locally.

**Q: Why do I need a proxy server?**
A: The proxy server helps bypass CORS issues when accessing the Ollama Serve API from a browser.

Feel free to reach out if you have any questions or need further assistance. Enjoy your journey with local LLMs!

---
