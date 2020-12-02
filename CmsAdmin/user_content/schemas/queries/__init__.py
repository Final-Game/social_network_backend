from core.authenticates.account_authentication import AccountAuthentication
from core.schemas.base_auth import BaseAuth, authenticate_permission
from user_content.domain.models.profile import Profile
from user_content.app.queries.get_account_profile_query import GetAccountProfileQuery
from core.app.bus import Bus
import graphene

from .test_type import TestType
from .account_profile_type import AccountProfileType


class Query(graphene.ObjectType, BaseAuth):

    authentication_classes = [AccountAuthentication]

    abc = graphene.Field(TestType)
    account_profile = graphene.Field(
        AccountProfileType,
        auth_token=graphene.String(required=True, description="Auth token"),
        account_id=graphene.String(required=True, description="Account Id"),
    )

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
