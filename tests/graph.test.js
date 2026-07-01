const Graph = require('../src/index');

describe('Graph with reflexivity', () => {
  let g;

  beforeEach(() => {
    g = new Graph();
  });

  test('adding a node creates reflexive edge', () => {
    g.addNode('A');
    expect(g.nodes()).toContain('A');
    expect(g.hasEdge('A', 'A')).toBe(true);
  });

  test('adding an edge between existing nodes', () => {
    g.addNode('A');
    g.addNode('B');
    g.addEdge('A', 'B');
    expect(g.hasEdge('A', 'B')).toBe(true);
    expect(g.hasEdge('B', 'A')).toBe(false);
  });

  test('adding an edge automatically adds missing nodes', () => {
    g.addEdge('X', 'Y');
    expect(g.nodes()).toEqual(expect.arrayContaining(['X', 'Y']));
    expect(g.hasEdge('X', 'Y')).toBe(true);
    // reflexive edges for both nodes
    expect(g.hasEdge('X', 'X')).toBe(true);
    expect(g.hasEdge('Y', 'Y')).toBe(true);
  });

  test('getNeighbors returns correct neighbors', () => {
    g.addNode('1');
    g.addNode('2');
    g.addEdge('1', '2');
    expect(g.getNeighbors('1')).toEqual(expect.arrayContaining(['1', '2']));
    expect(g.getNeighbors('2')).toEqual(['2']);
  });

  test('edges method returns all edges', () => {
    g.addNode('A');
    g.addNode('B');
    g.addEdge('A', 'B');
    const edges = g.edges();
    expect(edges).toEqual(
      expect.arrayContaining([
        ['A', 'A'],
        ['B', 'B'],
        ['A', 'B']
      ])
    );
    expect(edges.length).toBe(3);
  });
});