#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple LangGraph example that demonstrates reflection on code.
The graph has three nodes:
1. start_node - initializes the state.
2. reflect_node - introspects the source code of `target_function`.
3. end_node - prints the reflected source code.
"""

import inspect
from langgraph.graph import StateGraph, END

# Define a target function whose source code will be reflected.
def target_function(x: int, y: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return x + y

# Node definitions
def start_node(state: dict) -> dict:
    """
    Entry point of the graph. Sets an initial message.
    """
    state["message"] = "Graph started."
    return state

def reflect_node(state: dict) -> dict:
    """
    Retrieves the source code of `target_function` using inspect.
    Stores the source code in the state under the key 'source'.
    """
    source = inspect.getsource(target_function)
    state["source"] = source
    return state

def end_node(state: dict) -> dict:
    """
    Final node that prints the reflected source code.
    """
    print("\n=== Reflected Source Code ===")
    print(state.get("source", "No source found."))
    print("=============================\n")
    return state

# Build the graph
def build_graph() -> StateGraph:
    """
    Constructs and returns a LangGraph StateGraph with the defined nodes.
    """
    graph = StateGraph(dict)

    # Add nodes
    graph.add_node("start", start_node)
    graph.add_node("reflect", reflect_node)
    graph.add_node("end", end_node)

    # Define entry point and edges
    graph.set_entry_point("start")
    graph.add_edge("start", "reflect")
    graph.add_edge("reflect", "end")
    graph.add_edge("end", END)

    return graph

def main() -> None:
    """
    Main entry point for running the graph.
    """
    graph = build_graph()
    app = graph.compile()

    # Invoke the graph with an empty initial state
    try:
        result = app.invoke({})
        # The result contains the final state; we can inspect it if needed.
        # For this example, the end_node already prints the source code.
    except Exception as e:
        print(f"An error occurred while running the graph: {e}")

if __name__ == "__main__":
    main()