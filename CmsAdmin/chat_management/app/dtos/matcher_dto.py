from chat_management.app.dtos.media_dto import MediaDto
from dataclasses import dataclass
from typing import List


@dataclass
class MatcherDto:
    matcher_id: str
    name: str
    age: int
    bio: str
    status: int
    medias: List[MediaDto]