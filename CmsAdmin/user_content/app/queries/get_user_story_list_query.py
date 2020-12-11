from typing import List
from user_content.app.dtos.user_story_data_dto import UserStoryDataDto, UserStoryMedia
from user_content.domain.models.user_story import UserStory

from django.db.models.query_utils import Q
from core.app.bus import Query, QueryHandler
from user_content.models import Account


class UserStoryListMetadata(object):
    page: int
    limit: int

    def __init__(self, page: int = 0, limit: int = 10) -> None:
        self.page = page
        self.limit = limit


class GetUserStoryListQuery(Query):
    account_id: str
    metadata: UserStoryListMetadata

    def __init__(
        self, account_id: str, metadata: UserStoryListMetadata = UserStoryListMetadata()
    ) -> None:
        self.account_id = account_id
        self.metadata = metadata


class GetUserStoryListQueryHandler(QueryHandler):
    def handle(self, query: GetUserStoryListQuery) -> List[UserStoryDataDto]:
        account: Account = Account.objects.find_account_by_id(
            account_id=query.account_id, raise_exception=True
        )

        following_users_has_story: List[Account] = self.get_user_followers_has_story(
            account
        )
        return list(
            map(lambda x: map_account_to_user_story_data(x), following_users_has_story)
        )

    @staticmethod
    def get_user_followers_has_story(account: Account) -> UserStoryDataDto:
        following_users_queryset: List[Account] = account.following_users

        return following_users_queryset.filter(Q(userstory__isnull=False))


def map_account_to_user_story_data(account: Account):
    user_stories: List[UserStory] = list(
        filter(lambda x: x.is_visible(), list(account.userstory_set.all()))
    )

    media_datas: List[UserStoryMedia] = list(
        map(lambda x: UserStoryMedia(x.id, x.content, x.media_url), user_stories)
    )

    fullname: str = account.profile and account.profile.full_name
    return UserStoryDataDto(account.id, name=fullname, media_datas=media_datas)
