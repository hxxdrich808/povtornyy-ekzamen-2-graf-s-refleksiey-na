/**
 * Graph with reflexivity (self‑loops on every node).
 *
 * The graph is represented internally as an adjacency list using a Map.
 * Each node automatically has an edge to itself when it is added.
 *
 * Public API:
 *   - addNode(node): Adds a node and its reflexive edge.
 *   - addEdge(from, to): Adds a directed edge from `from` to `to`.
 *   - hasEdge(from, to): Returns true if an edge exists.
 *   - getNeighbors(node): Returns an array of all neighbors of `node`.
 *   - nodes(): Returns an array of all nodes in the graph.
 *   - edges(): Returns an array of [from, to] pairs representing all edges.
 */

class Graph {
  constructor() {
    /** @type {Map<any, Set<any>>} */
    this.adj = new Map();
  }

  /**
   * Adds a node to the graph. If the node already exists, nothing changes.
   * A reflexive edge (node → node) is automatically added.
   *
   * @param {any} node
   */
  addNode(node) {
    if (!this.adj.has(node)) {
      this.adj.set(node, new Set([node])); // reflexive edge
    }
  }

  /**
   * Adds a directed edge from `from` to `to`. If either node does not exist,
   * it is automatically added (with its reflexive edge).
   *
   * @param {any} from
   * @param {any} to
   */
  addEdge(from, to) {
    if (!this.adj.has(from)) this.addNode(from);
    if (!this.adj.has(to)) this.addNode(to);
    this.adj.get(from).add(to);
  }

  /**
   * Checks whether an edge from `from` to `to` exists.
   *
   * @param {any} from
   * @param {any} to
   * @returns {boolean}
   */
  hasEdge(from, to) {
    return this.adj.has(from) && this.adj.get(from).has(to);
  }

  /**
   * Returns an array of all neighbors of the given node.
   *
   * @param {any} node
   * @returns {any[]}
   */
  getNeighbors(node) {
    return this.adj.has(node) ? Array.from(this.adj.get(node)) : [];
  }

  /**
   * Returns an array of all nodes in the graph.
   *
   * @returns {any[]}
   */
  nodes() {
    return Array.from(this.adj.keys());
  }

  /**
   * Returns an array of all edges in the graph as [from, to] pairs.
   *
   * @returns {[any, any][]}
   */
  edges() {
    const edges = [];
    for (const [from, neighbors] of this.adj.entries()) {
      for (const to of neighbors) {
        edges.push([from, to]);
      }
    }
    return edges;
  }
}

module.exports = Graph;