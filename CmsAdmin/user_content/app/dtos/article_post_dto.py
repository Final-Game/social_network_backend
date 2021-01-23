from dataclasses import dataclass
from typing import List

from .media_data_dto import MediaDataDto as MediaData


@dataclass
class ArticlePostDto:
    id: str
    account_id: str
    content: str = ""
    medias: List[MediaData] = None
    user_comment_count: int = 0
    user_react_count: int = 0
