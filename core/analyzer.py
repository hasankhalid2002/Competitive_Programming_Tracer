from typing import List, Dict
from collections import Counter
from models.submission import Submission

class CodeforcesAnalyzer:
    def __init__(self, submissions: List[Submission]):
        self.submissions = submissions

    def get_verdict_stats(self) -> Dict[str, int]:
        verdicts = [sub.verdict for sub in self.submissions]
        return dict(Counter(verdicts))

    def get_acceptance_rate(self) -> float:
        if not self.submissions:
            return 0.0
        ok_count = sum(1 for sub in self.submissions if sub.verdict == "OK")
        return round((ok_count / len(self.submissions)) * 100, 2)

    def get_tag_distribution(self) -> Dict[str, int]:
        """Returns the frequency of each problem tag for ACCEPTED submissions."""
        tags = []
        for sub in self.submissions:
            if sub.verdict == "OK":
                tags.extend(sub.problem.tags)
        return dict(Counter(tags))

    def get_rating_distribution(self) -> Dict[int, int]:
        """Returns how many ACCEPTED problems solved per difficulty rating."""
        ratings = []
        for sub in self.submissions:
            if sub.verdict == "OK" and sub.problem.rating is not None:
                ratings.append(sub.problem.rating)
        return dict(sorted(Counter(ratings).items()))