from user_content.app.dtos.update_account_profile_dto import UpdateAccountProfileDto
from user_content.app.commands.update_account_profile_command import (
    UpdateAccountProfileCommand,
)
import graphene
from core.schemas.base_mutation import BaseMutation, authenticate_permission
from core.app.bus import Bus
from core.authenticates.account_authentication import AccountAuthentication

bus: Bus = Bus()


class UpdateAccountProfileMutation(BaseMutation):
    status = graphene.String(default_value="Success")

    authentication_classes = [AccountAuthentication]

    class Arguments:
        account_id = graphene.String(description="Account id", required=True)
        auth_token = graphene.String(description="Authenticate token")

        avatar_url = graphene.String(description="avatar url")
        cover_url = graphene.String(description="cover url")
        email = graphene.String(description="email")
        phone_number = graphene.String(description="phone number")
        first_name = graphene.String(description="first name")
        last_name = graphene.String(description="last name")
        gender = graphene.String(description="gender")
        marital_status = graphene.String(description="marital status")
        school = graphene.String(description="School")
        address = graphene.String(description="Address")
        bio = graphene.String(description="bio")
        birth_date = graphene.Date(description="birth date")

    @classmethod
    @authenticate_permission
    def mutate(cls, *args, **kwargs):
        account_id: str = kwargs.pop("account_id")

        global bus

        bus.dispatch(
            UpdateAccountProfileCommand(
                account_id, dto=UpdateAccountProfileDto(**kwargs)
            )
        )

        return cls()
