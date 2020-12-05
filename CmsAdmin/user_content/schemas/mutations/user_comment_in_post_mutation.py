from user_content.app.dtos.comment_dto import CommentDto
from user_content.app.commands.user_comment_in_post_command import (
    UserCommentInPostCommand,
)
from core.app.bus import Bus
from core.schemas.base_mutation import BaseMutation
import graphene
from core.schemas.base_auth import BaseAuth, authenticate_permission
from core.authenticates.account_authentication import AccountAuthentication


class CommentDataType(graphene.InputObjectType):
    base_id = graphene.String(description="Base comment id", required=False)
    content = graphene.String(description="content", required=True)


class UserCommentInPostMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        post_id = graphene.String(required=True, description="Post id")
        comment_data = CommentDataType(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        post_id: str = kwargs["post_id"]
        comment_data: dict = kwargs["comment_data"]

        bus: Bus = cls.get_bus()

        bus.dispatch(
            UserCommentInPostCommand(account_id, post_id, CommentDto(**comment_data))
        )

        return cls()
