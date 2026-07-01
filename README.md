# Graph with Reflexivity

A lightweight JavaScript implementation of a directed graph where every node automatically has a self‑loop (reflexive edge).  
The library is intentionally minimal and does **not** depend on any external graph libraries or Python code.

## Features

- **Automatic reflexivity** – when a node is added, an edge from the node to itself is created.
- **Directed edges** – you can add edges in any direction.
- **Simple API** – add nodes, add edges, query edges, list nodes, list edges.
- **Pure JavaScript** – works in Node.js environments.

## Installation

```bash
npm install graph-reflexivity
```

> If you want to run the tests or develop locally, clone the repository and run `npm install`.

## Usage

```js
const Graph = require('graph-reflexivity');

const g = new Graph();

// Add nodes
g.addNode('A');
g.addNode('B');

// Add directed edge A → B
g.addEdge('A', 'B');

// Reflexive edges are automatically added
console.log(g.hasEdge('A', 'A')); // true
console.log(g.hasEdge('B', 'B')); // true

// Query
console.log(g.getNeighbors('A')); // ['A', 'B']
console.log(g.nodes());          // ['A', 'B']
console.log(g.edges());          // [['A', 'A'], ['B', 'B'], ['A', 'B']]
```

## API

| Method | Description |
|--------|-------------|
| `addNode(node)` | Adds a node and its reflexive edge. |
| `addEdge(from, to)` | Adds a directed edge; missing nodes are created automatically. |
| `hasEdge(from, to)` | Returns `true` if an edge exists. |
| `getNeighbors(node)` | Returns an array of all neighbors of `node`. |
| `nodes()` | Returns an array of all nodes. |
| `edges()` | Returns an array of `[from, to]` pairs for all edges. |

## Testing

The project uses Jest for unit tests.

```bash
npm test
```

All tests are located in the `tests/` directory.

## License

MIT © Your Name

--- 

Feel free to open issues or pull requests if you find bugs or want to add features.