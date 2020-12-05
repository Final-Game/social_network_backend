from user_content.app.commands.user_delete_post_command import UserDeletePostCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserDeletePostMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description=" Authentication token")
        post_id = graphene.String(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        post_id: str = kwargs["post_id"]

        bus: Bus = cls.get_bus()
        bus.dispatch(UserDeletePostCommand(account_id, post_id))
        return super().mutate(*args, **kwargs)
