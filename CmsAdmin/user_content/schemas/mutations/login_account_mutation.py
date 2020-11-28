from user_content.app.dtos.login_account_response_dto import LoginAccountResponseDto
from user_content.app.dtos.login_account_dto import LoginAccountDto
from user_content.app.commands.login_account_command import LoginAccountCommand
import graphene
from core.app.bus import Bus

bus: Bus = Bus()


class LoginAccountMutation(graphene.Mutation):

    account_id = graphene.String(description="Account id")
    auth_token = graphene.String(description="Auth token to access data by user")
    refresh_token = graphene.String(description="Token is used to refresh new token")

    class Arguments:
        username = graphene.String(description="username", required=True)
        password = graphene.String(description="password")

    def mutate(self, *args, **kwargs):
        global bus
        login_response_dto: LoginAccountResponseDto = bus.dispatch(
            LoginAccountCommand(LoginAccountDto(**kwargs))
        )

        return LoginAccountMutation(**login_response_dto.to_dict())
