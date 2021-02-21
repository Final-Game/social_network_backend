from typing import List
from user_content.domain.models.user_story import UserStory
from user_content.app.dtos.user_story_data_dto import UserStoryDataDto, UserStoryMedia
from core.common.base_api_exception import BaseApiException
from user_content.domain.models.account import Account
from core.app.bus import Query, QueryHandler


class GetUserStoryQuery(Query):
    account_id: str
    partner_id: str

    def __init__(self, account_id: str, partner_id: str) -> None:
        self.account_id = account_id
        self.partner_id = partner_id


class GetUserStoryQueryHandler(QueryHandler):
    def handle(self, query: GetUserStoryQuery) -> UserStoryDataDto:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )
        partner: Account = Account.objects.find_account_by_id(
            query.partner_id, raise_exception=True
        )

        self.validate_account_can_view_stories_of_partner(account, partner)

        return map_account_to_user_story_data(partner)

    def validate_account_can_view_stories_of_partner(
        self, account: Account, partner: Account
    ):
        if account not in partner.followers.all():
            raise BaseApiException("Account can't view user story of this user.")

        if not partner.userstory_set.count():
            raise BaseApiException("This user don't have any stories.")


def map_account_to_user_story_data(account: Account) -> UserStoryDataDto:
    user_stories: List[UserStory] = list(
        filter(lambda x: x.is_visible(), list(account.userstory_set.all()))
    )

    media_datas: List[UserStoryMedia] = list(
        map(lambda x: UserStoryMedia(x.id, x.content, x.media_url), user_stories)
    )

    fullname: str = account.profile and account.profile.full_name or ""
    return UserStoryDataDto(account.id, name=fullname, media_datas=media_datas)