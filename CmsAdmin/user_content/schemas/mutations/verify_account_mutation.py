from user_content.app.dtos.account_verify_dto import AccountVerifyDto
from user_content.app.commands.verify_account_command import VerifyAccountCommand
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus
from core.authenticates.account_authentication import AccountAuthentication


class AccountVerifyTypeData(graphene.InputObjectType):
    front_photo_url = graphene.String(description="Front photo url")
    back_photo_url = graphene.String(description="Back photo url")


class AccountVerifyMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication Token")
        data = AccountVerifyTypeData(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]

        data: dict = kwargs.get("data", {})

        bus: Bus = cls.get_bus()
        bus.dispatch(VerifyAccountCommand(account_id, AccountVerifyDto(**data)))

        return cls()