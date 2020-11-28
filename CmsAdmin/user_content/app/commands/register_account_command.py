from core.common.base_api_exception import BaseApiException
from django.db import transaction

from core.app.bus import Command, CommandHandler

from user_content.domain.models.account import Account
from user_content.app.dtos.register_account_dto import RegisterAccountDto


class RegisterAccountCommand(Command):
    dto: RegisterAccountDto

    def __init__(self, dto: RegisterAccountDto) -> None:
        self.dto = dto

    def handler(self):
        return RegisterAccountCommandHandler


class RegisterAccountCommandHandler(CommandHandler):
    def handle(self, command: RegisterAccountCommand) -> bool:
        if not Account.check_email(command.dto.email):
            raise BaseApiException("This email is existed in system.")

        if not Account.check_username(command.dto.username):
            raise BaseApiException("This username is existed in system.")

        with transaction.atomic():
            new_account: Account = Account.new_normal_account(**command.dto.to_dict())
            new_account.save()
        return True
