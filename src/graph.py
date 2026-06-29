from langgraph.graph import StateGraph, END, START
from src.state import CodeReviewState
from src.nodes import draft_review, reflect, rewrite

def build_graph() -> StateGraph:
    graph = StateGraph(CodeReviewState)

    # Add nodes
    graph.add_node("draft_review", draft_review)
    graph.add_node("reflect", reflect)
    graph.add_node("rewrite", rewrite)

    # Define transitions
    graph.set_entry_point("draft_review")
    graph.add_edge("draft_review", "reflect")
    graph.add_conditional_edges(
        "reflect",
        lambda state: (
            "rewrite" if state["verdict"] == "needs_revision" and state["round"] < state["max_rounds"] else END
        ),
    )
    graph.add_edge("rewrite", "reflect")

    return graph