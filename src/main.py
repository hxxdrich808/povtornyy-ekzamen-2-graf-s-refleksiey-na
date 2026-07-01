#!/usr/bin/env python3
"""
Graph with reflection on code using LangGraph.

This script defines a simple LangGraph workflow that takes a code snippet,
passes it to an LLM for reflection, and outputs the reflection.

Requirements:
- langgraph
- langchain-openai
- openai

Set the environment variable OPENAI_API_KEY with your OpenAI API key.
"""

import os
from typing import Dict, Any

from langgraph.graph import StateGraph, END
from langchain_openai import OpenAI

# Define the state type for the graph
class CodeState(dict):
    """
    State dictionary that holds the code snippet and the reflection.
    """
    pass

def input_node(state: CodeState) -> Dict[str, Any]:
    """
    Entry node that simply passes the code snippet through.
    """
    # The state is expected to contain a 'code' key.
    return {"code": state.get("code", "")}

def reflection_node(state: CodeState) -> Dict[str, Any]:
    """
    Node that uses an LLM to generate a reflection on the provided code.
    """
    code = state.get("code", "")
    if not code:
        return {"reflection": "No code provided."}

    # Initialize the LLM
    llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")

    # Prompt the LLM to analyze the code and provide reflection
    prompt = (
        "You are an experienced software engineer. "
        "Analyze the following code snippet and provide a concise reflection "
        "on its structure, potential improvements, and any notable patterns.\n\n"
        f"{code}"
    )

    # Invoke the LLM
    response = llm.invoke(prompt)

    # The response is a string; store it in the state
    return {"reflection": response}

def output_node(state: CodeState) -> Dict[str, Any]:
    """
    Final node that simply returns the reflection.
    """
    return {"reflection": state.get("reflection", "")}

# Build the graph
graph = StateGraph(CodeState)

# Add nodes
graph.add_node("input", input_node)
graph.add_node("reflection", reflection_node)
graph.add_node("output", output_node)

# Define edges
graph.add_edge("input", "reflection")
graph.add_edge("reflection", "output")
graph.add_edge("output", END)

# Compile the graph into an executable app
app = graph.compile()

def run_graph(code_snippet: str) -> str:
    """
    Run the graph with the provided code snippet and return the reflection.
    """
    # Prepare the initial state
    initial_state = {"code": code_snippet}
    # Invoke the graph
    result = app.invoke(initial_state)
    # Extract the reflection
    return result.get("reflection", "")

if __name__ == "__main__":
    # Example usage
    sample_code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
    reflection = run_graph(sample_code)
    print("Reflection on code:")
    print(reflection)