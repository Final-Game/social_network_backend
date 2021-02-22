from user_content.domain.enums.react_type_enum import ReactTypeEnum
from user_content.domain.models.user_react_post import UserReactPost
from user_content.app.dtos.account_home_page_dto import AccountHomePageDto
from user_content.app.dtos.media_data_dto import MediaDataDto
from user_content.app.dtos.article_post_dto import ArticlePostDto
from core.common.pageable import Pageable
from dataclasses import dataclass
from typing import List

from django.db.models.query_utils import Q
from user_content.domain.models.post import Post
from user_content.domain.models.account import Account
from core.app.bus import Query, QueryHandler
from core.common.base_enum import BaseEnum


@dataclass
class HomePageMetadata:
    page: int = 0
    limit: int = 50


class GetAccountHomePageQuery(Query):
    account_id: str
    metadata: HomePageMetadata

    def __init__(
        self, account_id: str, metadata: HomePageMetadata = HomePageMetadata()
    ) -> None:
        self.account_id = account_id
        self.metadata = metadata


class GetAccountHomePageQueryHandler(QueryHandler):
    def handle(self, query: GetAccountHomePageQuery) -> AccountHomePageDto:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )

        return AccountHomePageDto(
            article_posts=list(
                map(
                    lambda x: map_post_model_to_article_post_dto(account, x),
                    self.get_related_posts(
                        account,
                        pageable=Pageable(query.metadata.page, query.metadata.limit),
                    ),
                )
            )
        )

    @staticmethod
    def get_related_posts(
        account: Account, pageable: Pageable = Pageable()
    ) -> List[Post]:
        offset_page: int = pageable.limit * pageable.page

        related_posts: List[Post] = Post.objects.filter(
            Q(account__in=account.following_users.all())
        ).order_by("-created_at")[offset_page : offset_page + pageable.limit]
        return list(related_posts)


def map_post_model_to_article_post_dto(account: Account, post: Post) -> ArticlePostDto:
    medias: List[MediaDataDto] = list(
        map(
            lambda x: MediaDataDto(url=x.url, type=map_media_type(x.type)),
            list(post.medias.all()),
        )
    )
    user_react_post: UserReactPost = UserReactPost.objects.filter(
        Q(sender=account) & Q(post=post)
    ).first()

    user_comment_count: int = post.usercommentpost_set.count()
    user_react_count: int = post.userreactpost_set.count()
    return ArticlePostDto(
        post.id,
        post.account_id,
        content=post.content,
        medias=medias,
        user_comment_count=user_comment_count,
        user_react_count=user_react_count,
        react_status=user_react_post
        and ReactTypeEnum.to_value(user_react_post.type)
        or None,
    )


class MediaTypeDto(BaseEnum):
    VIDEO: int = 1
    PHOTO: int = 0


def map_media_type(media_type: int) -> str:
    if media_type == MediaTypeDto.PHOTO:
        return MediaTypeDto.PHOTO.name
    elif media_type == MediaTypeDto.VIDEO:
        return MediaTypeDto.VIDEO.name