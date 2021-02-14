from chat_management.app.dtos.media_dto import MediaDto
from dataclasses import dataclass
from typing import List


@dataclass
class MatcherInfoDto:
    matcher_id: str
    name: str
    age: int
    gender: int
    address: str
    job: str
    reason: str
    medias: List[MediaDto]
    status: int = 1