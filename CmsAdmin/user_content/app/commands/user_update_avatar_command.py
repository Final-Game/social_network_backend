from user_content.domain.models.profile import Profile
from core.common.base_api_exception import BaseApiException
from user_content.domain.models.account import Account
from user_content.app.dtos.avatar_account_dto import AvatarAccountDto
from core.app.bus import Command, CommandHandler


class UserUpdateAvatarCommand(Command):
    account_id: str
    dto: AvatarAccountDto

    def __init__(self, account_id: str, dto: AvatarAccountDto) -> None:
        self.account_id = account_id
        self.dto = dto


class UserUpdateAvatarCommandHandler(CommandHandler):
    def handle(self, command: UserUpdateAvatarCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        if not account.profile:
            raise BaseApiException("Please update personal information.")

        account_profile: Profile = account.profile
        account_profile.update_avatar(command.dto.media_url)
        account.save()

        return super().handle(command)