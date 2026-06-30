/**
 * Graph implementation using adjacency list.
 * Each vertex automatically has a self-loop (reflexive edge).
 * The graph is undirected.
 */
class Graph {
  constructor() {
    /** @type {Map<*, Set<*>>} */
    this.adj = new Map();
  }

  /**
   * Adds a vertex to the graph.
   * If the vertex already exists, nothing changes.
   * A self-loop is automatically added to make the graph reflexive.
   * @param {*} v
   */
  addVertex(v) {
    if (!this.adj.has(v)) {
      this.adj.set(v, new Set([v]));
    }
  }

  /**
   * Adds an undirected edge between u and v.
   * Vertices are added automatically if they do not exist.
   * @param {*} u
   * @param {*} v
   */
  addEdge(u, v) {
    this.addVertex(u);
    this.addVertex(v);
    this.adj.get(u).add(v);
    this.adj.get(v).add(u);
  }

  /**
   * Removes the undirected edge between u and v.
   * If the edge does not exist, nothing happens.
   * @param {*} u
   * @param {*} v
   */
  removeEdge(u, v) {
    if (this.adj.has(u)) this.adj.get(u).delete(v);
    if (this.adj.has(v)) this.adj.get(v).delete(u);
  }

  /**
   * Removes a vertex and all incident edges.
   * @param {*} v
   */
  removeVertex(v) {
    if (!this.adj.has(v)) return;
    for (const neighbor of this.adj.get(v)) {
      if (neighbor !== v) this.adj.get(neighbor).delete(v);
    }
    this.adj.delete(v);
  }

  /**
   * Checks whether an edge exists between u and v.
   * @param {*} u
   * @param {*} v
   * @returns {boolean}
   */
  hasEdge(u, v) {
    return this.adj.has(u) && this.adj.get(u).has(v);
  }

  /**
   * Returns an array of neighbors of vertex v.
   * @param {*} v
   * @returns {Array<*>}
   */
  getNeighbors(v) {
    return this.adj.has(v) ? Array.from(this.adj.get(v)) : [];
  }

  /**
   * Returns an array of all vertices in the graph.
   * @returns {Array<*>}
   */
  vertices() {
    return Array.from(this.adj.keys());
  }

  /**
   * Returns an array of all edges as [u, v] pairs.
   * Each undirected edge appears only once.
   * @returns {Array<[*, *]>}
   */
  edges() {
    const edges = [];
    const seen = new Set();
    for (const [u, neighbors] of this.adj.entries()) {
      for (const v of neighbors) {
        const key = u < v ? `${u}-${v}` : `${v}-${u}`;
        if (!seen.has(key)) {
          edges.push([u, v]);
          seen.add(key);
        }
      }
    }
    return edges;
  }

  /**
   * Returns the number of vertices.
   * @returns {number}
   */
  size() {
    return this.adj.size;
  }

  /**
   * Returns the number of undirected edges.
   * @returns {number}
   */
  edgesCount() {
    return this.edges().length;
  }

  /**
   * Checks whether the graph is reflexive (every vertex has a self-loop).
   * @returns {boolean}
   */
  isReflexive() {
    for (const [v, neighbors] of this.adj.entries()) {
      if (!neighbors.has(v)) return false;
    }
    return true;
  }

  /**
   * Adds self-loops to all vertices, making the graph reflexive.
   */
  makeReflexive() {
    for (const v of this.adj.keys()) {
      this.adj.get(v).add(v);
    }
  }

  /**
   * Removes self-loops from all vertices.
   */
  removeReflexive() {
    for (const [v, neighbors] of this.adj.entries()) {
      neighbors.delete(v);
    }
  }
}

module.exports = Graph;