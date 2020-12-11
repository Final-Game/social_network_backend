from dataclasses import dataclass
from typing import List


@dataclass
class MediaDataDto:
    url: str
    type: int


@dataclass
class UserCommentDto:
    id: str
    asccount_id: str
    content: str


@dataclass
class PostReactDto:
    type: str
    account_ids: List[str]


@dataclass
class PostDetailDto:
    id: str
    content: str
    medias: List[MediaDataDto]
    user_comment_count: int
    user_react_count: int
    user_comments: List[UserCommentDto]
    user_reacts: List[PostReactDto]
