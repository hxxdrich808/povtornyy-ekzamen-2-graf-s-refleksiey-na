"""
Reflexive Graph Implementation using LangGraph

This module defines a simple graph data structure that supports adding nodes,
adding directed edges, and automatically adding reflexive edges (self-loops)
for each node. The implementation relies on the LangGraph library to
manage the underlying graph representation.

Author: Artur Kuzakhmetov
"""

from langgraph import Graph


class ReflexiveGraph:
    """
    A graph that automatically adds reflexive edges (self-loops) for each node.
    """

    def __init__(self):
        """
        Initialize an empty LangGraph instance.
        """
        self.graph = Graph()

    def add_node(self, node: str) -> None:
        """
        Add a node to the graph.

        Parameters
        ----------
        node : str
            The identifier of the node to add.
        """
        self.graph.add_node(node)

    def add_edge(self, src: str, dst: str) -> None:
        """
        Add a directed edge from src to dst.

        Parameters
        ----------
        src : str
            Source node identifier.
        dst : str
            Destination node identifier.
        """
        self.graph.add_edge(src, dst)

    def add_reflexive_edges(self) -> None:
        """
        Add a self-loop (reflexive edge) for every node in the graph.
        """
        for node in self.graph.nodes:
            self.graph.add_edge(node, node)

    def get_neighbors(self, node: str) -> list[str]:
        """
        Retrieve the successors (outgoing neighbors) of a given node.

        Parameters
        ----------
        node : str
            Node identifier.

        Returns
        -------
        list[str]
            List of successor node identifiers.
        """
        return list(self.graph.successors(node))

    def __repr__(self) -> str:
        """
        Return a string representation of the graph.
        """
        nodes = list(self.graph.nodes)
        edges = list(self.graph.edges)
        return f"ReflexiveGraph(nodes={nodes}, edges={edges})"


def main() -> None:
    """
    Demonstrate the usage of ReflexiveGraph.
    """
    rg = ReflexiveGraph()
    rg.add_node("A")
    rg.add_node("B")
    rg.add_node("C")

    rg.add_edge("A", "B")
    rg.add_edge("B", "C")

    # Add reflexive edges (self-loops)
    rg.add_reflexive_edges()

    print("Graph representation:")
    print(rg)

    print("\nNeighbors of node 'A':")
    print(rg.get_neighbors("A"))


if __name__ == "__main__":
    main()