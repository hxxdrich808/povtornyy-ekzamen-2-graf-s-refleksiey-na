import os
from src.graph import build_graph
from src.state import CodeReviewState

def main():
    # Example function to review
    def sort_numbers(arr):
        return sorted(arr)

    # Get source code as string
    import inspect
    code_str = inspect.getsource(sort_numbers)

    # Initial state
    state: CodeReviewState = {
        "code": code_str,
        "draft_review": None,
        "criteria_scores": None,
        "weakest_criterion": None,
        "verdict": None,
        "round": 0,
        "max_rounds": 2,
    }

    graph = build_graph()
    # Run the graph
    final_state = graph.invoke(state)

    # Print results
    print("\n=== Initial Draft Review ===")
    print(final_state["draft_review"])
    print("\n=== Scores ===")
    for k, v in final_state["criteria_scores"].items():
        print(f"{k}: {v}")
    print("\n=== Verdict ===")
    print(final_state["verdict"])
    print("\n=== Final Review (after rewrites if any) ===")
    print(final_state["draft_review"])

if __name__ == "__main__":
    main()