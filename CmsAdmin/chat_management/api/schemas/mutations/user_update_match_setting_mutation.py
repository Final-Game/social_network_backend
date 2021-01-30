from chat_management.app.dtos.match_setting_request_dto import MatchSettingRequestDto
from chat_management.app.commands.update_user_match_setting_command import (
    UpdateUserMatchSettingCommand,
)
from core.schemas.base_auth import authenticate_permission
import graphene
from core.schemas import BaseAuth, BaseMutation
from core.authenticates.account_authentication import AccountAuthentication
from core.app.bus import Bus


class UserUpdateMatchSettingMutation(BaseMutation, BaseAuth):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(required=True)
        auth_token = graphene.String(required=True, description="Authentication token")

        min_age = graphene.Int(required=True, description="Min age")
        max_age = graphene.Int(required=True, description="Max age")
        max_distance = graphene.Int(required=True, description="Max distance")
        target_gender = graphene.String(required=True, description="Gender")

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs["account_id"]

        min_age: int = kwargs["min_age"]
        max_age: int = kwargs["max_age"]
        max_dinstance: int = kwargs["max_distance"]
        target_gender: str = kwargs["target_gender"]

        _bus: Bus = cls.get_bus()

        _bus.dispatch(
            UpdateUserMatchSettingCommand(
                account_id,
                dto=MatchSettingRequestDto(
                    min_age, max_age, max_dinstance, target_gender
                ),
            )
        )

        return super().mutate(*args, **kwargs)
