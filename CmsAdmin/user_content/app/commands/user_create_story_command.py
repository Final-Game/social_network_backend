from user_content.domain.models.user_story import UserStory
from user_content.domain.models.account import Account
from user_content.app.dtos.user_story_dto import UserStoryDto
from core.app.bus import Command, CommandHandler
from django.db import transaction


class UserCreateStoryCommand(Command):
    account_id: str
    dto: UserStoryDto

    def __init__(self, account_id: str, dto: UserStoryDto) -> None:
        self.account_id = account_id
        self.dto = dto


class UserCreateStoryCommandHandler(CommandHandler):
    def handle(self, command: UserCreateStoryCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        with transaction.atomic():

            account.userstory_set.add(
                UserStory.objects.create(
                    content=command.dto.content, media_url=command.dto.media_url
                )
            )
            account.save()

        return super().handle(command)