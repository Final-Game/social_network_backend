from user_content.app.dtos.user_story_dto import UserStoryDto
from user_content.app.commands.user_create_story_command import UserCreateStoryCommand
from core.authenticates.account_authentication import AccountAuthentication
import graphene
from core.app.bus import Bus
from core.schemas.base_auth import BaseAuth, authenticate_permission
from core.schemas.base_mutation import BaseMutation


class UserStoryTypeData(graphene.InputObjectType):
    content = graphene.String(required=False, description="Content of story")
    media_url = graphene.String(required=False, description="Media url for story")


class UserCreateStoryMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")

        story_data = UserStoryTypeData(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        story_data: dict = kwargs["story_data"]

        bus: Bus = cls.get_bus()
        bus.dispatch(UserCreateStoryCommand(account_id, UserStoryDto(**story_data)))
        return super().mutate(*args, **kwargs)
