#!/usr/bin/env python3
"""
Graph implementation using an adjacency list.

This module defines a simple undirected graph data structure that
supports adding and removing nodes and edges, querying adjacency,
and iterating over nodes and edges.  The implementation uses a
single approach – an adjacency dictionary – and does not mix
alternative representations.

Author: Artur Kuzakhmetov
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, List, Set, Tuple


class Graph:
    """
    Undirected graph represented by an adjacency list.

    Nodes can be any hashable Python object.  Edges are stored
    as unordered pairs; self‑loops (reflexive edges) are allowed.
    """

    def __init__(self, nodes: Iterable = None, edges: Iterable[Tuple] = None):
        """
        Create a new graph.

        Parameters
        ----------
        nodes : Iterable, optional
            Iterable of initial nodes.
        edges : Iterable[Tuple], optional
            Iterable of initial edges, each edge is a tuple
            (node1, node2).  For self‑loops, node1 == node2.
        """
        self._adj: Dict = defaultdict(set)  # type: Dict[object, Set[object]]
        if nodes:
            for node in nodes:
                self.add_node(node)
        if edges:
            for n1, n2 in edges:
                self.add_edge(n1, n2)

    # ------------------------------------------------------------------
    # Node operations
    # ------------------------------------------------------------------
    def add_node(self, node: object) -> None:
        """Add a node to the graph.  If the node already exists, do nothing."""
        self._adj.setdefault(node, set())

    def remove_node(self, node: object) -> None:
        """Remove a node and all incident edges."""
        if node not in self._adj:
            raise KeyError(f"Node {node!r} not found")
        # Remove node from neighbors' adjacency sets
        for neighbor in list(self._adj[node]):
            self._adj[neighbor].discard(node)
        # Remove the node itself
        del self._adj[node]

    def nodes(self) -> Set[object]:
        """Return a set of all nodes in the graph."""
        return set(self._adj.keys())

    # ------------------------------------------------------------------
    # Edge operations
    # ------------------------------------------------------------------
    def add_edge(self, n1: object, n2: object) -> None:
        """
        Add an undirected edge between n1 and n2.

        If either node does not exist, it is created automatically.
        """
        self.add_node(n1)
        self.add_node(n2)
        self._adj[n1].add(n2)
        self._adj[n2].add(n1)

    def remove_edge(self, n1: object, n2: object) -> None:
        """Remove the edge between n1 and n2.  Raises KeyError if not present."""
        if n1 not in self._adj or n2 not in self._adj:
            raise KeyError("One or both nodes not found")
        if n2 not in self._adj[n1]:
            raise KeyError(f"Edge ({n1!r}, {n2!r}) does not exist")
        self._adj[n1].discard(n2)
        self._adj[n2].discard(n1)

    def has_edge(self, n1: object, n2: object) -> bool:
        """Return True if an edge exists between n1 and n2."""
        return n1 in self._adj and n2 in self._adj[n1]

    def edges(self) -> Set[Tuple[object, object]]:
        """Return a set of all edges as unordered tuples."""
        seen = set()
        for n, neighbors in self._adj.items():
            for m in neighbors:
                if (m, n) not in seen:
                    seen.add((n, m))
        return seen

    # ------------------------------------------------------------------
    # Adjacency queries
    # ------------------------------------------------------------------
    def neighbors(self, node: object) -> Set[object]:
        """Return the set of neighbors of the given node."""
        if node not in self._adj:
            raise KeyError(f"Node {node!r} not found")
        return set(self._adj[node])

    # ------------------------------------------------------------------
    # Utility methods
    # ------------------------------------------------------------------
    def __len__(self) -> int:
        """Return the number of nodes in the graph."""
        return len(self._adj)

    def __repr__(self) -> str:
        return f"Graph(nodes={list(self._adj.keys())}, edges={list(self.edges())})"

    def __str__(self) -> str:
        lines = [f"Graph with {len(self)} nodes and {len(self.edges())} edges:"]
        for node in sorted(self._adj):
            neigh = ", ".join(map(str, sorted(self._adj[node])))
            lines.append(f"  {node}: {neigh}")
        return "\n".join(lines)


# ----------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")  # triangle
    g.add_edge("D", "D")  # reflexive edge
    print(g)
    print("Neighbors of B:", g.neighbors("B"))
    print("Has edge (A, D)?", g.has_edge("A", "D"))
    g.remove_edge("A", "B")
    print("After removing edge (A, B):")
    print(g)
    g.remove_node("C")
    print("After removing node C:")
    print(g)