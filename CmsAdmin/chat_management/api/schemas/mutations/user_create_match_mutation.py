from chat_management.app.dtos.create_match_dto import CreateMatchDto
from chat_management.app.commands.create_user_match_command import (
    CreateUserMatchCommand,
)
from core.app.bus import Bus
from core.schemas.base_auth import authenticate_permission
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.authenticates.account_authentication import AccountAuthentication


class UserCreateMatchMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")

        receiver_id = graphene.String(required=True, description="Receiver id")
        status = graphene.Int(
            required=True, description="0 - close, 1- love, 2 - super love"
        )

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]

        receiver_id: str = kwargs["receiver_id"]
        status: int = kwargs["status"]

        _bus: Bus = cls.get_bus()

        _bus.dispatch(
            CreateUserMatchCommand(account_id, dto=CreateMatchDto(receiver_id, status))
        )

        return cls()