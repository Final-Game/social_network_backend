from core.common.base_api_exception import BaseApiException
from user_content.domain.models.account import Account
from user_content.app.dtos.change_account_password_dto import ChangeAccountPasswordDto
from core.app.bus import Command, CommandHandler
from django.contrib.auth.hashers import check_password


class ChangeAccountPasswordCommand(Command):
    account_id: str
    dto: ChangeAccountPasswordDto

    def __init__(self, account_id: str, dto: ChangeAccountPasswordDto) -> None:
        self.account_id = account_id
        self.dto = dto


class ChangeAccountPasswordCommandHandler(CommandHandler):
    def handle(self, command: ChangeAccountPasswordCommand) -> bool:
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )

        if not check_password(command.dto.old_password, account.password):
            raise BaseApiException("Old password is incorrect.")

        account.change_password(command.dto.new_password)
        account.save()

        return True
