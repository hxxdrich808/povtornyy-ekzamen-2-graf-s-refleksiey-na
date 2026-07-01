// src/graph.js
// A simple graph implementation with reflexive edge support
// This module is pure JavaScript and can be used in both Node and browser environments.

export class Graph {
  constructor() {
    // adjacency list: nodeId -> Set of neighbor nodeIds
    this.adj = new Map();
    // node properties: nodeId -> {label, ...}
    this.nodes = new Map();
  }

  // Add a node with optional properties
  addNode(id, props = {}) {
    if (this.nodes.has(id)) {
      throw new Error(`Node ${id} already exists`);
    }
    this.nodes.set(id, { id, ...props });
    this.adj.set(id, new Set());
  }

  // Add a directed edge from src to dst
  addEdge(src, dst) {
    if (!this.nodes.has(src) || !this.nodes.has(dst)) {
      throw new Error(`Both nodes must exist to add an edge: ${src} -> ${dst}`);
    }
    this.adj.get(src).add(dst);
  }

  // Return array of neighbor ids for a node
  neighbors(id) {
    if (!this.adj.has(id)) return [];
    return Array.from(this.adj.get(id));
  }

  // Add reflexive edges (self-loops) to all nodes
  addReflexiveEdges() {
    for (const id of this.nodes.keys()) {
      this.adj.get(id).add(id);
    }
  }

  // Return a plain object representation (useful for serialization)
  toJSON() {
    const nodes = Array.from(this.nodes.values());
    const edges = [];
    for (const [src, dstSet] of this.adj.entries()) {
      for (const dst of dstSet) {
        edges.push({ src, dst });
      }
    }
    return { nodes, edges };
  }

  // Static helper to create a graph from a JSON representation
  static fromJSON(json) {
    const g = new Graph();
    for (const node of json.nodes) {
      g.addNode(node.id, node);
    }
    for (const edge of json.edges) {
      g.addEdge(edge.src, edge.dst);
    }
    return g;
  }
}