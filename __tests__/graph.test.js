// __tests__/graph.test.js
import { Graph } from '../src/graph.js';

describe('Graph', () => {
  let g;

  beforeEach(() => {
    g = new Graph();
    g.addNode('1', { label: 'One' });
    g.addNode('2', { label: 'Two' });
    g.addNode('3', { label: 'Three' });
  });

  test('adds nodes correctly', () => {
    expect(g.nodes.size).toBe(3);
    expect(g.nodes.get('1').label).toBe('One');
  });

  test('adds edges correctly', () => {
    g.addEdge('1', '2');
    g.addEdge('2', '3');
    expect(g.neighbors('1')).toEqual(['2']);
    expect(g.neighbors('2')).toEqual(['3']);
    expect(g.neighbors('3')).toEqual([]);
  });

  test('throws error when adding edge with non-existent node', () => {
    expect(() => g.addEdge('1', '4')).toThrow();
  });

  test('adds reflexive edges', () => {
    g.addReflexiveEdges();
    expect(g.neighbors('1')).toContain('1');
    expect(g.neighbors('2')).toContain('2');
    expect(g.neighbors('3')).toContain('3');
  });

  test('toJSON returns correct structure', () => {
    g.addEdge('1', '2');
    const json = g.toJSON();
    expect(json.nodes).toHaveLength(3);
    expect(json.edges).toHaveLength(1);
    expect(json.edges[0]).toEqual({ src: '1', dst: '2' });
  });

  test('fromJSON recreates graph', () => {
    g.addEdge('1', '2');
    const json = g.toJSON();
    const g2 = Graph.fromJSON(json);
    expect(g2.nodes.size).toBe(3);
    expect(g2.neighbors('1')).toEqual(['2']);
  });
});