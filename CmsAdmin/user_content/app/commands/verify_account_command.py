from user_content.domain.models.account_verify import AccountVerify
from user_content.domain.models.account import Account
from user_content.app.dtos.account_verify_dto import AccountVerifyDto
from core.app.bus import Command, CommandHandler


class VerifyAccountCommand(Command):
    account_id: str
    dto: AccountVerifyDto

    def __init__(self, account_id: str, dto: AccountVerifyDto) -> None:
        self.account_id = account_id
        self.dto = dto


class VerifyAccountCommandHandler(CommandHandler):
    def handle(self, command: VerifyAccountCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )

        account_verify: AccountVerify = getattr(
            account, "accountverify", None
        ) or AccountVerify(account=account)

        account_verify.update_data(**command.dto.__dict__)
        account_verify.set_pending()
        account_verify.save()