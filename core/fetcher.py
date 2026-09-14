import requests
from typing import List, Dict, Any
from core.exceptions import UserNotFoundException, APIConnectionException
from models.user import UserProfile
from models.submission import Submission, Problem

class CodeforcesFetcher:
    BASE_URL = "https://codeforces.com/api"

    def fetch_user_profile(self, handle: str) -> UserProfile:
        url = f"{self.BASE_URL}/user.info?handles={handle}"
        data = self._make_request(url)
        
        user_raw = data["result"][0]
        return UserProfile(
            handle=user_raw.get("handle", handle),
            rating=user_raw.get("rating", 0),
            max_rating=user_raw.get("maxRating", 0),
            rank=user_raw.get("rank", "unrated"),
            avatar_url=user_raw.get("avatar", ""),
            title_photo_url=user_raw.get("titlePhoto", "")
        )

    def fetch_user_submissions(self, handle: str) -> List[Submission]:
        url = f"{self.BASE_URL}/user.status?handle={handle}"
        data = self._make_request(url)
        
        submissions = []
        for sub in data["result"]:
            prob_raw = sub.get("problem", {})
            problem = Problem(
                contest_id=prob_raw.get("contestId"),
                index=prob_raw.get("index", ""),
                name=prob_raw.get("name", ""),
                rating=prob_raw.get("rating"),
                tags=prob_raw.get("tags", [])
            )
            
            submissions.append(
                Submission(
                    id=sub["id"],
                    contest_id=sub.get("contestId"),
                    creation_time_seconds=sub["creationTimeSeconds"],
                    verdict=sub.get("verdict", "UNKNOWN"),
                    problem=problem
                )
            )
        return submissions

    def _make_request(self, url: str) -> Dict[str, Any]:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 400:
                raise UserNotFoundException("Handle not found on Codeforces.")
            response.raise_for_status()
            
            payload = response.json()
            if payload.get("status") != "OK":
                raise APIConnectionException("Codeforces API returned an error status.")
                
            return payload
        except requests.exceptions.RequestException as e:
            raise APIConnectionException(f"Network error occurred: {e}")