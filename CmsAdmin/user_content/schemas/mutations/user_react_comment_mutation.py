from user_content.app.dtos.user_react_comment_dto import UserReactCommentDto
from user_content.app.commands.user_react_comment_command import UserReactCommentCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus

from core.authenticates.account_authentication import AccountAuthentication


class UserReactCommentTypeData(graphene.InputObjectType):
    type = graphene.String(description="LIKE/LOVE")


class UserReactCommentMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")
        comment_id = graphene.String(required=True, description="Comment id")

        react_data = UserReactCommentTypeData(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        comment_id: str = kwargs["comment_id"]

        react_data: dict = kwargs["react_data"]

        bus: Bus = cls.get_bus()
        bus.dispatch(
            UserReactCommentCommand(
                account_id, comment_id, UserReactCommentDto(**react_data)
            )
        )

        return cls()
