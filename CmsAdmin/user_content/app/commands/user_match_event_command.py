from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler
from django.db import transaction


class UserMatchEventCommand(Command):
    account_id: str
    partner_id: str

    def __init__(self, account_id: str, partner_id: str) -> None:
        self.account_id = account_id
        self.partner_id = partner_id


class UserMatchEventCommandHandler(CommandHandler):
    def handle(self, command: UserMatchEventCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        partner: Account = Account.objects.find_account_by_id(
            command.partner_id, raise_exception=True
        )

        with transaction.atomic():
            self.follow_users(account, partner)

    @staticmethod
    def follow_users(account: Account, partner: Account):
        account.follow(partner)
        partner.follow(account)
