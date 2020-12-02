from user_content.app.dtos.change_account_password_dto import ChangeAccountPasswordDto
from user_content.app.commands.change_account_password_command import (
    ChangeAccountPasswordCommand,
)
from core.authenticates.account_authentication import AccountAuthentication
import graphene
from core.app.bus import Bus
from core.schemas.base_auth import BaseAuth, authenticate_permission

bus: Bus = Bus()


class ChangeAccountPasswordMutation(graphene.Mutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(description="Account id", required=True)
        auth_token = graphene.String(description="Authenticate token")
        old_password = graphene.String(description="Old password", required=True)
        new_password = graphene.String(description="New password", required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]

        bus.dispatch(
            ChangeAccountPasswordCommand(
                account_id,
                dto=ChangeAccountPasswordDto(
                    kwargs["old_password"], kwargs["new_password"]
                ),
            )
        )
        return cls()