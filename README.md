# LangGraph Reflection Example

This repository demonstrates a simple **LangGraph** workflow that performs reflection on a Python function's source code. The graph consists of three nodes:

1. **start_node** – Initializes the graph state.
2. **reflect_node** – Uses Python's `inspect` module to retrieve the source code of `target_function`.
3. **end_node** – Prints the reflected source code.

## Requirements

- Python 3.x
- `langchain_openai`
- `langchain_core`
- `langgraph`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Running the Example

```bash
python src/main.py
```

You should see the source code of `target_function` printed to the console.

## Project Structure

```
├── requirements.txt
├── src
│   ├── __init__.py
│   └── main.py
└── README.md
```

No JavaScript code is included; the entire project is implemented in Python using the LangGraph framework.