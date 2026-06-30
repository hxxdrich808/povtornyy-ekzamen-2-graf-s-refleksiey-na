# Graph with Reflection on Code

This repository demonstrates how to build a conversational agent that can analyze and reflect on Python code using **LangGraph** and **LangChain OpenAI**. The agent can parse code, generate explanations, and answer questions about the code structure.

## Features

- **LangGraph**: Orchestrates the conversation flow and manages state across multiple turns.
- **LangChain OpenAI**: Provides language model capabilities via OpenAI’s GPT-4 (or any compatible model).
- Code parsing and analysis using the `ast` module.
- Interactive CLI for asking questions about a Python file.

## Getting Started

### Prerequisites

- Python 3.10+
- An OpenAI API key. Set it in your environment:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

### Installation

```bash
# Clone the repository
git clone https://git.brojs.ru/kuzakhmetovartur/povtornyy-ekzamen-2-graf-s-refleksiey-na.git
cd povtornyy-ekzamen-2-graf-s-refleksiey-na

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

`requirements.txt` contains:

```
langchain==0.2.0
langgraph==0.1.0
openai==1.0.0
```

### Usage

Run the main script and provide the path to a Python file you want to analyze:

```bash
python main.py path/to/your_script.py
```

You will be prompted to ask questions about the code. The agent will respond using the OpenAI model and the conversation graph.

### Example

```bash
$ python main.py example.py
Enter your question (or type 'exit' to quit): What does the `add` function do?
The `add` function takes two numbers, `a` and `b`, and returns their sum.
```

## Project Structure

```
povtornyy-ekzamen-2-graf-s-refleksiey-na/
├── main.py          # Entry point
├── code_analyzer.py # Code parsing utilities
├── graph.py         # LangGraph definition
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*This project was developed as part of a coursework assignment. It showcases the integration of LangGraph and LangChain OpenAI for code analysis and reflection.*