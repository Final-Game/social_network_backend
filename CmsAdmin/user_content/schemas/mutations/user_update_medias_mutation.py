from user_content.app.dtos.media_data_dto import MediaDataDto
from user_content.app.commands.user_update_medias_command import UserUpdateMediasCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus
from core.authenticates.account_authentication import AccountAuthentication


class MediaAccountType(graphene.InputObjectType):
    url = graphene.String(description="Media url", required=True)
    type = graphene.String(description="Type of media: PHOTO, VIDEO")


class UserUpdateMediasMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")

        medias = graphene.List(MediaAccountType, required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        media_datas: list = kwargs["medias"]

        _bus: Bus = cls.get_bus()
        _bus.dispatch(
            UserUpdateMediasCommand(
                account_id, medias=list(map(lambda x: MediaDataDto(**x), media_datas))
            )
        )
        return cls()