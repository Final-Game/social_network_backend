from core.common.base_api_exception import BaseApiException
from user_content.domain.models.user_story import UserStory
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler


class UserDeleteStoryCommand(Command):
    account_id: str
    story_id: str

    def __init__(self, account_id: str, story_id: str) -> None:
        self.account_id = account_id
        self.story_id = story_id


class UserDeleteStoryCommandHandler(CommandHandler):
    def handle(self, command: UserDeleteStoryCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        story: UserStory = UserStory.objects.find_story_by_id(
            command.story_id, raise_exception=True
        )
        self.validate_user_can_remove_story(account, story)

        story.delete()

        return True

    @classmethod
    def validate_user_can_remove_story(cls, account: Account, story: UserStory):
        owner_story: Account = story.account

        if account != owner_story:
            raise BaseApiException("Can't remove story. Permission denied.")
