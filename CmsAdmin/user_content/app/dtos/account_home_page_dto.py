from dataclasses import dataclass
from typing import List
from .article_post_dto import ArticlePostDto


@dataclass
class AccountHomePageDto:
    article_posts: List[ArticlePostDto]