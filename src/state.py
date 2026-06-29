from typing import TypedDict, Dict, Any

class CodeReviewState(TypedDict):
    code: str
    draft_review: str | None
    criteria_scores: Dict[str, int] | None
    weakest_criterion: str | None
    verdict: str | None  # "ok" | "needs_revision"
    round: int
    max_rounds: int