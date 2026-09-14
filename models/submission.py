from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Problem:
    contest_id: Optional[int]
    index: str
    name: str
    rating: Optional[int]
    tags: List[str]

@dataclass
class Submission:
    id: int
    contest_id: Optional[int]
    creation_time_seconds: int
    verdict: str  # OK, WRONG_ANSWER, TIME_LIMIT_EXCEEDED...
    problem: Problem