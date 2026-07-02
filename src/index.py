"""
LangGraph Code Review Agent with Reflection – Graph-Based Implementation

This project demonstrates a simple code review agent that uses LangGraph's
graph-based approach exclusively. The original repository mixed both the
graph-based and chain-based paradigms; this refactor removes all chain
references and consolidates the logic into a single graph.

Key points:
- Only the graph API (`langgraph.graph.StateGraph`) is used.
- No chain imports or chain-based logic remain.
- The graph consists of three nodes:
    1. `review` – performs the initial code review.
    2. `reflect` – reflects on the review output.
    3. `output` – returns the final response.
- The agent uses OpenAI's ChatCompletion model via `langchain_openai.ChatOpenAI`.
  An environment variable `OPENAI_API_KEY` must be set for the LLM to work.
"""

import os
from typing import Dict, List, Any

from langgraph.graph import StateGraph, CompiledGraph
from langgraph.prebuilt import create_chat_agent
from langchain_openai import ChatOpenAI

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

# Ensure the OpenAI API key is available
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY environment variable is not set. "
        "Please set it to your OpenAI API key."
    )

# LLM configuration
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=OPENAI_API_KEY,
)

# --------------------------------------------------------------------------- #
# State definition
# --------------------------------------------------------------------------- #

# The graph state will contain a list of messages that the LLM will see.
# Each message is a dict with "role" and "content" keys, following the
# OpenAI chat format.
State = Dict[str, List[Dict[str, str]]]


# --------------------------------------------------------------------------- #
# Node definitions
# --------------------------------------------------------------------------- #

def review_node(state: State) -> State:
    """
    Node that performs the initial code review.

    It receives the current state, appends a system prompt asking for a
    code review, and returns the updated state.
    """
    # Append system prompt for review
    review_prompt = {
        "role": "system",
        "content": (
            "You are a senior software engineer. "
            "Please review the following code snippet and provide constructive feedback."
        ),
    }
    # Append user message containing the code to review
    user_message = {
        "role": "user",
        "content": state["messages"][-1]["content"],  # The code snippet
    }

    # Build the messages for the LLM
    messages = state["messages"] + [review_prompt, user_message]

    # Call the LLM
    response = llm.invoke(messages)

    # Append the LLM's response to the state
    state["messages"] = messages + [
        {"role": "assistant", "content": response.content}
    ]

    return state


def reflect_node(state: State) -> State:
    """
    Node that reflects on the review output.

    It asks the LLM to reflect on the review and suggest improvements.
    """
    # Append system prompt for reflection
    reflect_prompt = {
        "role": "system",
        "content": (
            "You are a senior software engineer. "
            "Reflect on the previous review and suggest any additional improvements."
        ),
    }

    # Build the messages for the LLM
    messages = state["messages"] + [reflect_prompt]

    # Call the LLM
    response = llm.invoke(messages)

    # Append the LLM's reflection to the state
    state["messages"] = messages + [
        {"role": "assistant", "content": response.content}
    ]

    return state


def output_node(state: State) -> Dict[str, Any]:
    """
    Final node that extracts the assistant's last message as the output.
    """
    # The last assistant message contains the reflection
    last_message = state["messages"][-1]["content"]
    return {"final_output": last_message}


# --------------------------------------------------------------------------- #
# Graph construction
# --------------------------------------------------------------------------- #

def build_graph() -> CompiledGraph:
    """
    Constructs and compiles the LangGraph graph.
    """
    graph = StateGraph(State)

    # Add nodes
    graph.add_node("review", review_node)
    graph.add_node("reflect", reflect_node)
    graph.add_node("output", output_node)

    # Define edges
    graph.set_entry_point("review")
    graph.add_edge("review", "reflect")
    graph.add_edge("reflect", "output")

    # Compile the graph for execution
    return graph.compile()


# --------------------------------------------------------------------------- #
# Main execution
# --------------------------------------------------------------------------- #

def main() -> None:
    """
    Entry point for the agent.

    Reads a code snippet from a file named `sample_code.py` in the project root
    and runs the graph to produce a review and reflection.
    """
    # Load code snippet
    code_path = os.path.join(os.path.dirname(__file__), "..", "sample_code.py")
    if not os.path.exists(code_path):
        raise FileNotFoundError(
            f"Sample code file not found at {code_path}. "
            "Please provide a 'sample_code.py' file with code to review."
        )

    with open(code_path, "r", encoding="utf-8") as f:
        code_snippet = f.read()

    # Initial state: only the code snippet as a user message
    initial_state: State = {
        "messages": [
            {"role": "user", "content": code_snippet}
        ]
    }

    # Build and run the graph
    graph = build_graph()
    result = graph.invoke(initial_state)

    # Print the final output
    print("\n=== Code Review and Reflection ===\n")
    print(result["final_output"])


if __name__ == "__main__":
    main()