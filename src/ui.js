// src/ui.js
// Simple UI rendering using D3.js
// Assumes D3 is loaded globally (e.g., via CDN in index.html)

export function renderGraph(graph, containerId) {
  const container = document.getElementById(containerId);
  if (!container) {
    throw new Error(`Container with id "${containerId}" not found`);
  }

  // Clear previous content
  container.innerHTML = '';

  const width = container.clientWidth || 600;
  const height = container.clientHeight || 400;

  const svg = d3.select(container)
    .append('svg')
    .attr('width', width)
    .attr('height', height);

  const nodes = graph.nodes.values();
  const edges = [];
  for (const [src, dstSet] of graph.adj.entries()) {
    for (const dst of dstSet) {
      edges.push({ source: src, target: dst });
    }
  }

  // Simple force simulation for layout
  const simulation = d3.forceSimulation(Array.from(nodes))
    .force('link', d3.forceLink(edges).id(d => d.id).distance(120))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2));

  const link = svg.append('g')
    .attr('class', 'links')
    .selectAll('line')
    .data(edges)
    .enter()
    .append('line')
    .attr('stroke', '#999')
    .attr('stroke-width', 1.5);

  const node = svg.append('g')
    .attr('class', 'nodes')
    .selectAll('circle')
    .data(Array.from(nodes))
    .enter()
    .append('circle')
    .attr('r', 20)
    .attr('fill', '#69b3a2')
    .call(d3.drag()
      .on('start', dragstarted)
      .on('drag', dragged)
      .on('end', dragended));

  const label = svg.append('g')
    .attr('class', 'labels')
    .selectAll('text')
    .data(Array.from(nodes))
    .enter()
    .append('text')
    .attr('dy', 4)
    .attr('text-anchor', 'middle')
    .text(d => d.label || d.id);

  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);

    label
      .attr('x', d => d.x)
      .attr('y', d => d.y);
  });

  function dragstarted(event, d) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  }

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  }

  function dragended(event, d) {
    if (!event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  }
}