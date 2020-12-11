from typing import List
from user_content.domain.enums.react_type_enum import ReactTypeEnum
from user_content.app.dtos.post_detail_dto import (
    MediaDataDto,
    PostDetailDto,
    PostReactDto,
    UserCommentDto,
)
from user_content.domain.models.post import Post
from user_content.domain.models.account import Account
from core.app.bus import Query, QueryHandler


class GetPostDetailQuery(Query):
    account_id: str
    post_id: str

    def __init__(self, account_id: str, post_id: str) -> None:
        self.account_id = account_id
        self.post_id = post_id


class GetPostDetailQueryHandler(QueryHandler):
    def handle(self, query: GetPostDetailQuery) -> PostDetailDto:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )
        post: Post = Post.objects.find_post_by_id(query.post_id, raise_exception=True)
        self.validate_account_can_view_post(account, post)

        return map_post_model_to_post_detail_dto(post)

    @staticmethod
    def validate_account_can_view_post(account: Account, post: Post):
        # TODO Can add block user feature to active this rule.
        return


def map_post_model_to_post_detail_dto(post: Post) -> PostDetailDto:
    medias: List[MediaDataDto] = list(
        map(lambda x: MediaDataDto(url=x.url, type=x.type), list(post.medias.all()))
    )

    user_comment_count: int = post.usercommentpost_set.count()
    user_react_count: int = post.userreactpost_set.count()

    user_comments: List[UserCommentDto] = list(
        map(
            lambda x: UserCommentDto(x.id, x.sender_id, x.content),
            list(post.usercommentpost_set.all()),
        )
    )

    # extract user react data
    user_react_datas: dict = {}
    for urp in post.userreactpost_set.all():
        type_name: str = ReactTypeEnum.to_value(urp.type)
        if not type_name:
            continue

        if type_name not in user_react_datas.keys():
            user_react_datas.update({type_name: []})

        user_react_datas[type_name].append(urp.sender_id)

    user_reacts: List[PostReactDto] = list(
        map(
            lambda x: PostReactDto(type=x, account_ids=user_react_datas[x]),
            list(user_react_datas.keys()),
        )
    )

    return PostDetailDto(
        post.id,
        post.content,
        medias,
        user_comment_count,
        user_react_count,
        user_comments,
        user_reacts,
    )
