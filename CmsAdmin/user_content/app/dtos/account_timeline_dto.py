from dataclasses import dataclass
from typing import List


@dataclass
class MediaData:
    url: str
    type: int


@dataclass
class ArticlePost:
    id: str
    account_id: str
    content: str = ""
    medias: List[MediaData] = None


@dataclass
class AccountTimeLineDto:
    article_posts: ArticlePost