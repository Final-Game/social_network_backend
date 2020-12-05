from user_content.app.dtos.react_tory_dto import ReactStoryDto
from user_content.app.commands.user_view_story_command import UserViewStoryCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserReactStoryTypeData(graphene.InputObjectType):
    type = graphene.String(description="LIKE/LOVE")


class UserViewStoryMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication Token")
        story_id = graphene.String(required=True, description="Story id")
        react_data = UserReactStoryTypeData(required=False)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        story_id: str = kwargs["story_id"]
        react_data: dict = kwargs.get("react_data", {})

        bus: Bus = cls.get_bus()
        bus.dispatch(
            UserViewStoryCommand(account_id, story_id, ReactStoryDto(**react_data))
        )
        return super().mutate(*args, **kwargs)