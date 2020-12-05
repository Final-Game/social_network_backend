from user_content.domain.models.story_viewer import StoryViewer
from user_content.app.dtos.react_tory_dto import ReactStoryDto
from django.db import transaction

from core.common.base_api_exception import BaseApiException
from user_content.domain.models.user_story import UserStory
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler


class UserViewStoryCommand(Command):
    account_id: str
    story_id: str
    dto: ReactStoryDto

    def __init__(
        self, account_id: str, story_id: str, dto: ReactStoryDto = ReactStoryDto()
    ) -> None:
        self.account_id = account_id
        self.story_id = story_id
        self.dto = dto


class UserViewStoryCommandHandler(CommandHandler):
    def handle(self, command: UserViewStoryCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        story: UserStory = UserStory.objects.find_story_by_id(
            command.story_id, raise_exception=True
        )
        self.validate_user_can_view_story(account, story)

        with transaction.atomic():
            if account not in story.viewers.all():
                story.viewers.add(account)
                story.save()
            storyviewer: StoryViewer = StoryViewer.objects.get(
                story=story, viewer=account
            )
            storyviewer.change_react_type(command.dto.type)
            storyviewer.save()

        return True

    def validate_user_can_view_story(self, account: Account, story: UserStory):
        if not story.is_visible():
            raise BaseApiException("Story was disabled")