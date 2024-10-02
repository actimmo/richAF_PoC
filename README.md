# README

## Program Overview

This Python program processes stock news articles using the Ollama language model. It takes input either from a file or directly from the user, sends the text to the model for analysis, and receives a JSON response. The response predicts whether the article is relevant for stock analysis, the potential stock movement direction, and the confidence in that prediction.

The program uses the following:
- **subprocess** for running external commands (the Ollama model).
- **json** for handling the structured response from the model.
- **sys** for handling command-line arguments and input.

## Requirements

### Prerequisites
- Python 3.x
- Ollama model "llama3.1:latest"
- Basic terminal/command-line knowledge

### Python Packages:
- None beyond standard libraries (`subprocess`, `json`, `sys`)

### Setup
1. Install the Ollama tool and configure it on your system. The program is designed to run the Ollama model via command-line.
2. Ensure that you have the appropriate model 'llama3.1:latest' is installed
3. Run the model or install it by calling 'ollama serve' followed by 'ollama run llama3.1:latest'

## Usage

### Command-Line Usage:
```bash
python your_program.py [input_file]