# Graph with Reflection on Code

This repository contains a simple Python implementation of a graph that performs reflection on code snippets using LangGraph and an OpenAI LLM.

## Requirements

- Python 3.10+
- `langgraph`
- `langchain-openai`
- `openai`

## Setup

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Running the Graph

The graph is defined in `src/main.py`. To run it with a sample code snippet:

```bash
python src/main.py
```

You should see a reflection printed to the console.

## Using the Graph Programmatically

You can import the `run_graph` function from `src/main.py` and pass any code snippet:

```python
from src.main import run_graph

code = """
def add(a, b):
    return a + b
"""

reflection = run_graph(code)
print(reflection)
```

## How Reflection Works

The graph has three nodes:

1. **Input Node** – Receives the code snippet.
2. **Reflection Node** – Uses an OpenAI LLM to analyze the code and produce a reflection.
3. **Output Node** – Returns the reflection.

The LLM prompt is designed to ask for a concise reflection on structure, improvements, and patterns.

## License

MIT License