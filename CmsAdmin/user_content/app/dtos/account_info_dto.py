from datetime import date
from dataclasses import dataclass
from typing import List


@dataclass
class MediaDto:
    url: str
    type: int


@dataclass
class AccountInfoDto:
    id: str
    full_name: str
    avatar: str
    birth_date: date
    gender: int
    medias: List[MediaDto]
    bio: str = ""
    address: str = ""
    job: str = ""
    reason: str = ""