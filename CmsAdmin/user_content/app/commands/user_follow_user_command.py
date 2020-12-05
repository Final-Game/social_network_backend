from core.common.base_api_exception import BaseApiException
from django.db import transaction
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler


class UserFollowUserCommand(Command):
    account_id: str
    target_id: str

    def __init__(self, account_id: str, target_id: str) -> None:
        self.account_id = account_id
        self.target_id = target_id

        self.validate()

    def validate(self):
        if self.account_id == self.target_id:
            raise BaseApiException("Can't follow owner.")


class UserFollowUserCommandHandler(CommandHandler):
    def handle(self, command: UserFollowUserCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        target_account: Account = Account.objects.find_account_by_id(
            command.target_id, raise_exception=True
        )
        self.validate_user_can_follow_user(account, target_account)

        with transaction.atomic():
            if account not in target_account.followers.all():
                target_account.followers.add(account)
                target_account.save()

        return True

    def validate_user_can_follow_user(self, account: Account, target: Account):
        return