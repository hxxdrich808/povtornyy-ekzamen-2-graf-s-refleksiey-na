# Graph with Reflection on Code – Refactored Implementation

This repository contains a minimal, self‑contained Python implementation of an undirected graph that uses a single, consistent approach: an adjacency list represented by a dictionary of sets.  
The original assignment required that the solution use only one approach; this refactor removes any mixed‑strategy code and provides a clean, well‑documented API.

## Features

- **Add / remove nodes** – Nodes are any hashable Python objects.
- **Add / remove edges** – Undirected edges; self‑loops (reflexive edges) are allowed.
- **Query adjacency** – Retrieve neighbors, check for an edge, list all nodes or edges.
- **Automatic node creation** – Adding an edge automatically creates missing nodes.
- **Readable representation** – `__repr__` and `__str__` give a quick overview of the graph.

## Usage

```python
from src.index import Graph

# Create an empty graph
g = Graph()

# Add edges (nodes are created automatically)
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("C", "A")  # triangle
g.add_edge("D", "D")  # reflexive edge

print(g)  # Pretty print

# Query
print("Neighbors of B:", g.neighbors("B"))
print("Has edge (A, D)?", g.has_edge("A", "D"))

# Modify
g.remove_edge("A", "B")
g.remove_node("C")

print("After modifications:")
print(g)
```

## Running the Example

```bash
python -m src.index
```

The script will output the graph state after each operation.

## Project Structure

```
src/
└── index.py   # Graph implementation
README.md      # Documentation
```

## License

This project is released under the MIT License.