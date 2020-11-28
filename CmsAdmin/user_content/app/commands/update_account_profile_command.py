from user_content.domain.models.account import Account
from user_content.app.dtos.update_account_profile_dto import UpdateAccountProfileDto
from core.app.bus import Command, CommandHandler


class UpdateAccountProfileCommand(Command):
    account_id: str
    dto: UpdateAccountProfileDto

    def __init__(self, account_id: str, dto: UpdateAccountProfileDto) -> None:
        self.account_id = account_id
        self.dto = dto


class UpdateAccountProfileCommandHandler(CommandHandler):
    def handle(self, command: UpdateAccountProfileCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )

        account.profile.update_data(**command.dto.map_to_profile_model_data())
        account.save()

        return True