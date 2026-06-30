const { createGraph } = require('../src/index');

describe('Graph with reflection', () => {
  let graph;
  beforeEach(() => {
    graph = createGraph();
  });

  test('initial log is empty', () => {
    expect(graph.getLog()).toEqual([]);
  });

  test('addNode records operation', () => {
    graph.addNode('a');
    expect(graph.getLog()).toEqual([{ method: 'addNode', args: ['a'] }]);
    expect(graph.getNodes()).toEqual(['a']);
  });

  test('addEdge records operation and creates nodes', () => {
    graph.addEdge('a', 'b');
    expect(graph.getLog()).toEqual([{ method: 'addEdge', args: ['a', 'b'] }]);
    expect(graph.getNodes().sort()).toEqual(['a', 'b']);
    expect(graph.getNeighbors('a')).toEqual(['b']);
    expect(graph.getNeighbors('b')).toEqual(['a']);
    expect(graph.hasEdge('a', 'b')).toBe(true);
  });

  test('removeEdge records operation', () => {
    graph.addEdge('a', 'b');
    graph.removeEdge('a', 'b');
    expect(graph.getLog()).toEqual([
      { method: 'addEdge', args: ['a', 'b'] },
      { method: 'removeEdge', args: ['a', 'b'] }
    ]);
    expect(graph.hasEdge('a', 'b')).toBe(false);
  });

  test('removeNode records operation and removes edges', () => {
    graph.addEdge('a', 'b');
    graph.addEdge('a', 'c');
    graph.removeNode('a');
    expect(graph.getLog()).toEqual([
      { method: 'addEdge', args: ['a', 'b'] },
      { method: 'addEdge', args: ['a', 'c'] },
      { method: 'removeNode', args: ['a'] }
    ]);
    expect(graph.getNodes().sort()).toEqual(['b', 'c']);
    expect(graph.getNeighbors('b')).toEqual([]);
    expect(graph.getNeighbors('c')).toEqual([]);
  });

  test('getNeighbors does not record operation', () => {
    graph.addNode('a');
    graph.getNeighbors('a');
    expect(graph.getLog()).toEqual([{ method: 'addNode', args: ['a'] }]);
  });

  test('log is a copy and not affected by external mutation', () => {
    graph.addNode('a');
    const log = graph.getLog();
    log.push({ method: 'fake', args: [] });
    expect(graph.getLog()).toEqual([{ method: 'addNode', args: ['a'] }]);
  });

  test('graph uses adjacency list internally', () => {
    graph.addNode('a');
    expect(graph.adj instanceof Map).toBe(true);
    expect(graph.adj.get('a') instanceof Set).toBe(true);
  });

  test('handles duplicate nodes and edges gracefully', () => {
    graph.addNode('a');
    graph.addNode('a');
    expect(graph.getNodes()).toEqual(['a']);
    graph.addEdge('a', 'a');
    expect(graph.hasEdge('a', 'a')).toBe(true);
    graph.addEdge('a', 'a');
    expect(graph.getNeighbors('a')).toEqual(['a']);
  });

  test('handles non-existing nodes and edges', () => {
    expect(graph.getNeighbors('x')).toEqual([]);
    expect(graph.hasEdge('x', 'y')).toBe(false);
    graph.removeEdge('x', 'y'); // should not throw
    graph.removeNode('x'); // should not throw
  });
});