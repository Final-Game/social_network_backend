from user_content.app.dtos.report_user_dto import ReportUserDto
from user_content.app.commands.report_user_command import ReportUserCommand
import graphene

from core.schemas import BaseAuth, BaseMutation
from core.schemas.base_auth import authenticate_permission
from core.app.bus import Bus
from core.authenticates.account_authentication import AccountAuthentication


class ReportUserDataType(graphene.InputObjectType):
    receiver_id = graphene.String(description="Receiver id", required=True)
    related_post_id = graphene.String(description="Related post id")
    reason = graphene.String(description="Reason", required=True)


class ReportUserMutaion(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(description="Account id", required=True)
        auth_token = graphene.String(description="Authencation token", required=True)

        data = ReportUserDataType(required=True)

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]
        data: dict = kwargs["data"]

        _bus: Bus = cls.get_bus()
        _bus.dispatch(ReportUserCommand(account_id, ReportUserDto(**data)))
        return cls()
