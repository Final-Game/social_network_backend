from user_content.app.dtos.avatar_account_dto import AvatarAccountDto
from user_content.app.commands.user_update_avatar_command import UserUpdateAvatarCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus
from core.authenticates.account_authentication import AccountAuthentication


class AvatarMediaAccountType(graphene.InputObjectType):
    media_url = graphene.String(description="Media url", required=True)
    type = graphene.String(description="type of media: PHOTO, VIDEO")


class UserUpdateAvatarMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")

        data = AvatarMediaAccountType(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        data: dict = kwargs["data"]

        _bus: Bus = cls.get_bus()
        _bus.dispatch(UserUpdateAvatarCommand(account_id, AvatarAccountDto(**data)))
        return cls()
