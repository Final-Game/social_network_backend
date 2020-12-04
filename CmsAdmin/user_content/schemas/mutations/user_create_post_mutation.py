from user_content.app.dtos.user_create_post_dto import MediaPostData, UserCreatePostDto
from user_content.app.commands.user_create_post_command import UserCreatePostCommand
import graphene
from graphene.types.objecttype import ObjectType
from core.app.bus import Bus
from core.schemas.base_auth import BaseAuth, authenticate_permission
from core.authenticates.account_authentication import AccountAuthentication

bus: Bus = Bus()


class MediaPostType(graphene.InputObjectType):
    url = graphene.String(description="Media url", required=True)
    type = graphene.Int(description="Type of media: 0-photo, 1-video")


class UserCreatePostMutation(graphene.Mutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(description="Account id", required=True)
        auth_token = graphene.String(description="Authen token", required=True)
        content = graphene.String(description="Description")
        medias = graphene.List(MediaPostType, description="Media datas")

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]

        cnt: str = kwargs["content"]
        media_datas: list = kwargs["medias"]
        bus.dispatch(
            UserCreatePostCommand(
                account_id,
                dto=UserCreatePostDto(
                    cnt,
                    media_datas=list(map(lambda x: MediaPostData(**x), media_datas)),
                ),
            )
        )

        return cls()
