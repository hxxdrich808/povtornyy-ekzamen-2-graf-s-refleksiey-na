// src/index.js
// Entry point for the application
import { Graph } from './graph.js';
import { renderGraph } from './ui.js';

document.addEventListener('DOMContentLoaded', () => {
  // Create a sample graph
  const g = new Graph();
  g.addNode('A', { label: 'Node A' });
  g.addNode('B', { label: 'Node B' });
  g.addNode('C', { label: 'Node C' });
  g.addNode('D', { label: 'Node D' });

  g.addEdge('A', 'B');
  g.addEdge('B', 'C');
  g.addEdge('C', 'D');
  g.addEdge('D', 'A');

  // Add reflexive edges (self-loops)
  g.addReflexiveEdges();

  // Render the graph into the container with id "graph-container"
  renderGraph(g, 'graph-container');
});