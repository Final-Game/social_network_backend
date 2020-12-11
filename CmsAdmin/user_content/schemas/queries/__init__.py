from typing import List
from user_content.app.queries.get_account_timeline_query import (
    AccountTimeLineMetadata,
    GetAccountTimeLineQuery,
)
from user_content.app.dtos.account_timeline_dto import AccountTimeLineDto
from user_content.app.queries.get_user_story_list_query import (
    GetUserStoryListQuery,
    GetUserStoryListQueryHandler,
    UserStoryListMetadata,
)
from user_content.app.dtos.user_story_data_dto import UserStoryDataDto
from user_content.app.queries.get_user_follow_list_query import (
    GetUserFollowListQuery,
    UserFollowMetadata,
)
from user_content.domain.models.account import Account
from core.authenticates.account_authentication import AccountAuthentication
from core.schemas.base_auth import BaseAuth, authenticate_permission
from user_content.domain.models.profile import Profile
from user_content.app.queries.get_account_profile_query import GetAccountProfileQuery
from core.app.bus import Bus
import graphene

from .test_type import TestType
from .account_profile_type import AccountProfileType
from .user_follow_type import UserFollowType
from .user_story_data_type import UserStoryDataType
from .account_timeline_type import AccountTimeLineType

auth_data: dict = {
    "auth_token": graphene.String(required=True, description="Auth token"),
    "account_id": graphene.String(required=True, description="Account id"),
}


class Query(graphene.ObjectType, BaseAuth):

    authentication_classes = [AccountAuthentication]

    abc = graphene.Field(TestType)
    account_profile = graphene.Field(
        AccountProfileType,
        auth_token=graphene.String(required=True, description="Auth token"),
        account_id=graphene.String(required=True, description="Account Id"),
    )
    user_followers = graphene.List(UserFollowType, **auth_data)
    user_stories = graphene.List(UserStoryDataType, **auth_data)
    account_timeline = graphene.Field(AccountTimeLineType, **auth_data)

    @classmethod
    def get_bus(cls):
        return Bus()

    def resolve_abc(self, *args, **kwargs):
        return TestType(x="Nguyen Minh Tuan")

    @classmethod
    @authenticate_permission
    def resolve_account_profile(cls, *args, **kwargs):
        __bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        account_profile: Profile = __bus.dispatch(GetAccountProfileQuery(account_id))

        return account_profile

    @classmethod
    @authenticate_permission
    def resolve_user_followers(cls, *args, **kwargs):
        __bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        user_followes: List[Account] = __bus.dispatch(
            GetUserFollowListQuery(account_id, UserFollowMetadata(page=0, limit=15))
        )

        return user_followes

    @classmethod
    @authenticate_permission
    def resolve_user_stories(cls, *args, **kwargs):
        __bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        user_stories: List[UserStoryDataDto] = __bus.dispatch(
            GetUserStoryListQuery(account_id, UserStoryListMetadata(page=0, limit=10))
        )

        return list(map(lambda x: x.to_dict(), user_stories))

    @classmethod
    @authenticate_permission
    def resolve_account_timeline(cls, *args, **kwargs):
        __bus: Bus = cls.get_bus()

        account_id: str = kwargs["account_id"]
        account_timeline: AccountTimeLineDto = __bus.dispatch(
            GetAccountTimeLineQuery(
                account_id, AccountTimeLineMetadata(page=0, limit=10)
            )
        )

        return account_timeline.__dict__
