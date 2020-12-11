from dataclasses import dataclass
from typing import List
from user_content.app.dtos.account_timeline_dto import (
    AccountTimeLineDto,
    ArticlePost,
    MediaData,
)
from user_content.domain.models.post import Post
from user_content.domain.models.account import Account
from core.app.bus import Query, QueryHandler


@dataclass
class AccountTimeLineMetadata:
    page: int = 0
    limit: int = 10


class GetAccountTimeLineQuery(Query):
    account_id: str
    metadata: AccountTimeLineMetadata

    def __init__(self, account_id: str, metadata: AccountTimeLineMetadata) -> None:
        self.account_id = account_id
        self.metadata = metadata


class GetAccountTimeLineQueryHandler(QueryHandler):
    def handle(self, query: GetAccountTimeLineQuery) -> AccountTimeLineDto:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )

        return AccountTimeLineDto(
            article_posts=list(
                map(
                    lambda x: map_post_model_to_article_post_dto(x),
                    account.article_posts,
                )
            )
        )


def map_post_model_to_article_post_dto(post: Post) -> ArticlePost:
    medias: List[MediaData] = list(
        map(lambda x: MediaData(url=x.url, type=x.type), list(post.medias.all()))
    )
    return ArticlePost(post.id, post.account_id, content=post.content, medias=medias)
