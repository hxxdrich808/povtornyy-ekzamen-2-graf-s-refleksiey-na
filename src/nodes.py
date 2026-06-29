from typing import Dict, Any
from langgraph.graph import StateGraph, END, START
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser
from src.state import CodeReviewState

# LLM instance
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Prompt for draft review
draft_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a senior code reviewer. Provide a concise review with 3-6 bullet points."),
        ("human", "Here is the Python function:\n\n{code}\n\nWrite your review:"),
    ]
)

# Prompt for reflection (scoring)
reflect_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a code quality critic. Evaluate the following review on four criteria: PEP8, type hints, edge cases, naming. Provide scores 0-10 and a verdict 'ok' or 'needs_revision'. Output JSON with keys: pep8, type_hints, edge_cases, naming, verdict."),
        ("human", "Review:\n\n{draft_review}\n\nScores:"),
    ]
)

# Prompt for rewrite
rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a code reviewer tasked with improving the weakest part of the review. Keep other points unchanged."),
        ("human", "Weakest criterion: {weakest_criterion}\n\nOriginal review:\n\n{draft_review}\n\nRewrite the section addressing the weakest criterion:"),
    ]
)

# Output parser for reflection
json_parser = JsonOutputParser()

def draft_review(state: CodeReviewState) -> CodeReviewState:
    """Generate initial draft review."""
    messages = draft_prompt.format_messages(code=state["code"])
    review = llm.invoke(messages).content
    state["draft_review"] = review.strip()
    state["round"] = 0
    return state

def reflect(state: CodeReviewState) -> CodeReviewState:
    """Score the draft review."""
    messages = reflect_prompt.format_messages(draft_review=state["draft_review"])
    raw_output = llm.invoke(messages).content
    try:
        scores = json_parser.parse(raw_output)
    except Exception as e:
        # Fallback: if parsing fails, set default scores
        scores = {
            "pep8": 0,
            "type_hints": 0,
            "edge_cases": 0,
            "naming": 0,
            "verdict": "needs_revision",
        }
    # Determine weakest criterion
    criteria = ["pep8", "type_hints", "edge_cases", "naming"]
    weakest = min(criteria, key=lambda c: scores[c])
    state["criteria_scores"] = {c: int(scores[c]) for c in criteria}
    state["weakest_criterion"] = weakest
    state["verdict"] = scores["verdict"]
    return state

def rewrite(state: CodeReviewState) -> CodeReviewState:
    """Rewrite the weakest part of the review."""
    messages = rewrite_prompt.format_messages(
        weakest_criterion=state["weakest_criterion"],
        draft_review=state["draft_review"],
    )
    rewritten = llm.invoke(messages).content
    # Replace the section related to weakest criterion
    # For simplicity, we just append the rewritten part to the original review
    state["draft_review"] = f"{state['draft_review']}\n\nImproved {state['weakest_criterion']} section:\n{rewritten.strip()}"
    state["round"] += 1
    return state