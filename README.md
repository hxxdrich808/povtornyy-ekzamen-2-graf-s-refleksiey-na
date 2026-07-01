# Reflexive Graph Implementation using LangGraph

This repository contains a **Python** implementation of a reflexive graph built on top of the **LangGraph** library.  
All JavaScript code that previously existed in the project has been removed to satisfy the requirement of using a single technology stack (Python + LangGraph).

## Features

- **Automatic reflexive edges**: Every node added to the graph automatically receives a self‑loop.
- **Directed edges**: Supports adding directed edges between nodes.
- **Neighbor queries**: Retrieve successors (outgoing neighbors) of any node.
- **Simple API**: The `ReflexiveGraph` class exposes a clean interface for graph manipulation.

## Installation

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install langgraph
```

> **Note**: The `langgraph` package must be available on PyPI. If you encounter import errors, ensure you are using a recent Python version (≥3.8) and that the package name is correct.

## Usage

```python
from src.main import ReflexiveGraph

def main() -> None:
    rg = ReflexiveGraph()
    rg.add_node("A")
    rg.add_node("B")
    rg.add_node("C")

    rg.add_edge("A", "B")
    rg.add_edge("B", "C")

    # Add reflexive edges (self‑loops)
    rg.add_reflexive_edges()

    print("Graph representation:")
    print(rg)

    print("\nNeighbors of node 'A':")
    print(rg.get_neighbors("A"))

if __name__ == "__main__":
    main()
```

Running the script will output the graph representation and the neighbors of node `A`.

## Project Structure

```
.
├── src
│   └── main.py          # Python implementation of the reflexive graph
└── README.md            # Project documentation
```

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

--- 

**Important**: This repository now contains **only Python code**. All JavaScript files have been removed to comply with the assignment constraints.