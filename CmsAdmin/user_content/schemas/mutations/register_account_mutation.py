from user_content.app.dtos.register_account_dto import RegisterAccountDto
from user_content.app.commands.register_account_command import RegisterAccountCommand
import graphene

from core.app.bus import Bus

bus: Bus = Bus()


class RegisterAccountMutation(graphene.Mutation):

    status = graphene.String(default_value="Success")

    class Arguments:
        username = graphene.String(description="User name", required=True)
        password = graphene.String(required=True, description="Password")
        email = graphene.String(required=False, description="Email")

    def mutate(self, *args, **kwargs):
        global bus
        bus.dispatch(RegisterAccountCommand(RegisterAccountDto(**kwargs)))

        return RegisterAccountMutation()