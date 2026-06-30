class Graph {
  constructor() {
    this.adj = new Map();
    this[Graph._logSymbol] = [];
  }

  addNode(node) {
    if (!this.adj.has(node)) {
      this.adj.set(node, new Set());
    }
  }

  addEdge(u, v) {
    if (!this.adj.has(u)) this.adj.set(u, new Set());
    if (!this.adj.has(v)) this.adj.set(v, new Set());

    const uSet = this.adj.get(u);
    const vSet = this.adj.get(v);

    if (!uSet.has(v)) {
      uSet.add(v);
      vSet.add(u);
    }
  }

  removeNode(node) {
    if (!this.adj.has(node)) return;
    for (const neighbor of this.adj.get(node)) {
      this.adj.get(neighbor).delete(node);
    }
    this.adj.delete(node);
  }

  removeEdge(u, v) {
    if (this.adj.has(u)) this.adj.get(u).delete(v);
    if (this.adj.has(v)) this.adj.get(v).delete(u);
  }

  getNeighbors(node) {
    return this.adj.has(node) ? Array.from(this.adj.get(node)) : [];
  }

  hasEdge(u, v) {
    return this.adj.has(u) && this.adj.get(u).has(v);
  }

  getNodes() {
    return Array.from(this.adj.keys());
  }

  getLog() {
    return this[Graph._logSymbol].slice();
  }
}

Graph._logSymbol = Symbol('log');

function createGraph() {
  const graph = new Graph();

  const handler = {
    get(target, prop, receiver) {
      const value = target[prop];
      if (typeof value === 'function') {
        // Mutating methods that should be logged
        if (['addNode', 'addEdge', 'removeNode', 'removeEdge'].includes(prop)) {
          return function (...args) {
            const result = value.apply(target, args);
            target[Graph._logSymbol].push({ method: prop, args });
            return result;
          };
        }
        // Non-mutating methods (including getLog)
        return value.bind(target);
      }
      return value;
    },
  };

  return new Proxy(graph, handler);
}

module.exports = { Graph, createGraph };