const { Graph } = require('../src');

describe('Graph', () => {
  let g;

  beforeEach(() => {
    g = new Graph();
  });

  test('initially empty', () => {
    expect(g.size()).toBe(0);
    expect(g.edgesCount()).toBe(0);
  });

  test('addVertex increases size and adds reflexive edge', () => {
    g.addVertex('a');
    expect(g.size()).toBe(1);
    expect(g.isReflexive()).toBe(true);
    expect(g.hasEdge('a', 'a')).toBe(true);
  });

  test('addEdge connects vertices and updates adjacency', () => {
    g.addEdge('a', 'b');
    expect(g.size()).toBe(2);
    expect(g.hasEdge('a', 'b')).toBe(true);
    expect(g.hasEdge('b', 'a')).toBe(true);
    expect(g.getNeighbors('a')).toEqual(expect.arrayContaining(['a', 'b']));
    expect(g.getNeighbors('b')).toEqual(expect.arrayContaining(['a', 'b']));
  });

  test('removeEdge removes connection', () => {
    g.addEdge('a', 'b');
    g.removeEdge('a', 'b');
    expect(g.hasEdge('a', 'b')).toBe(false);
    expect(g.hasEdge('b', 'a')).toBe(false);
    // self-loops remain
    expect(g.hasEdge('a', 'a')).toBe(true);
    expect(g.hasEdge('b', 'b')).toBe(true);
  });

  test('removeVertex removes vertex and incident edges', () => {
    g.addEdge('a', 'b');
    g.addEdge('a', 'c');
    g.removeVertex('a');
    expect(g.size()).toBe(2);
    expect(g.hasEdge('b', 'a')).toBe(false);
    expect(g.hasEdge('c', 'a')).toBe(false);
    expect(g.hasEdge('b', 'c')).toBe(false);
  });

  test('edges and edgesCount work correctly', () => {
    g.addEdge('a', 'b');
    g.addEdge('b', 'c');
    g.addEdge('c', 'a');
    expect(g.edgesCount()).toBe(3);
    const edges = g.edges();
    expect(edges).toEqual(expect.arrayContaining([
      ['a', 'b'],
      ['b', 'c'],
      ['c', 'a']
    ]));
  });

  test('self-loop handling', () => {
    g.addVertex('x');
    expect(g.hasEdge('x', 'x')).toBe(true);
    g.removeEdge('x', 'x');
    expect(g.hasEdge('x', 'x')).toBe(false);
  });

  test('reflexivity can be toggled', () => {
    g.addVertex('p');
    g.addVertex('q');
    g.removeReflexive();
    expect(g.isReflexive()).toBe(false);
    g.makeReflexive();
    expect(g.isReflexive()).toBe(true);
  });
});