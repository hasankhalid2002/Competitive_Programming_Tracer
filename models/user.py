from dataclasses import dataclass
from typing import Optional

@dataclass
class UserProfile:
    handle: str
    rating: int
    max_rating: int
    rank: str
    avatar_url: str
    title_photo_url: str