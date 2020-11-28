from user_content.app.dtos.login_account_response_dto import LoginAccountResponseDto
from core.common.base_api_exception import BaseApiException
from django.contrib.auth.hashers import check_password

from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler

from user_content.app.dtos import LoginAccountDto


class LoginAccountCommand(Command):
    dto: LoginAccountDto

    def __init__(self, dto: LoginAccountDto) -> None:
        self.dto = dto


class LoginAccountCommandHandler(CommandHandler):
    def handle(self, command: LoginAccountCommand) -> LoginAccountResponseDto:

        existed_account: Account = (
            Account.objects.find_account_by_username(
                command.dto.username, raise_exception=True
            )
            or None
        )

        if not check_password(command.dto.password, existed_account.password):
            raise BaseApiException("Wrong password.")

        return LoginAccountResponseDto(
            account_id=str(existed_account.id), **existed_account.generate_token()
        )
