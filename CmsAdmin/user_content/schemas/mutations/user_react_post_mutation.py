from user_content.app.dtos.user_react_post_dto import UserReactPostDto
from user_content.app.commands.user_react_post_command import UserReactPostCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserReactTypeData(graphene.InputObjectType):
    type = graphene.String(description="LIKE/LOVE")


class UserReactPostMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        post_id = graphene.String(required=True, description="Post id")

        react_data = UserReactTypeData(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        post_id: str = kwargs["post_id"]

        react_data: dict = kwargs["react_data"]

        bus: Bus = cls.get_bus()
        bus.dispatch(
            UserReactPostCommand(account_id, post_id, UserReactPostDto(**react_data))
        )

        return cls()
