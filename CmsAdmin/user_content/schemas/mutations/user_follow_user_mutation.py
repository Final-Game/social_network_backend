from user_content.app.commands.user_follow_user_command import UserFollowUserCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserFollowUserMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        target_id = graphene.String(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        target_id: str = kwargs["target_id"]

        bus: Bus = cls.get_bus()
        bus.dispatch(UserFollowUserCommand(account_id, target_id))

        return cls()