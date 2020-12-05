from user_content.app.commands import UserDeleteStoryCommand

import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserDeleteStoryMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        story_id = graphene.String(required=True, description="Story id")

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        story_id: str = kwargs["story_id"]

        bus: Bus = cls.get_bus()
        bus.dispatch(UserDeleteStoryCommand(account_id, story_id))
        return super().mutate(*args, **kwargs)
