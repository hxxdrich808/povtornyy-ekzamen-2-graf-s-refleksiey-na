# Graph with Reflection

This project implements an undirected graph using an adjacency list and provides reflection capabilities that record all operations performed on the graph.

## Features

- **Adjacency List**: Efficient storage and traversal of graph nodes and edges.
- **Reflection**: Every mutating operation (`addNode`, `addEdge`, `removeNode`, `removeEdge`) is logged.
- **API**:
  - `addNode(node)`
  - `addEdge(u, v)`
  - `removeNode(node)`
  - `removeEdge(u, v)`
  - `getNeighbors(node)`
  - `hasEdge(u, v)`
  - `getNodes()`
  - `getLog()` – returns a copy of the operation log.

## Installation

```bash
npm install
```

## Running Tests

```bash
npm test
```

## Usage

```js
const { createGraph } = require('./src/index');

const graph = createGraph();

graph.addNode('a');
graph.addNode('b');
graph.addEdge('a', 'b');

console.log(graph.getNeighbors('a')); // ['b']
console.log(graph.getLog());
// [
//   { method: 'addNode', args: ['a'] },
//   { method: 'addNode', args: ['b'] },
//   { method: 'addEdge', args: ['a', 'b'] }
// ]
```

The `getLog()` method returns a snapshot of all recorded operations, allowing you to inspect the history of changes made to the graph.