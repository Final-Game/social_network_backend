from dataclasses import dataclass
from typing import List

from .article_post_dto import ArticlePostDto as ArticlePost
from .media_data_dto import MediaDataDto as MediaData


@dataclass
class AccountTimeLineDto:
    article_posts: List[ArticlePost]