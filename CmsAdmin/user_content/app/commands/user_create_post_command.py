from user_content.gateways.services.media_service_impl import MediaServiceImpl
from user_content.app.services.media_service import MediaService
from user_content.domain.models.account import Account
from user_content.domain.models.post import Post
from user_content.app.dtos.user_create_post_dto import UserCreatePostDto
from core.app.bus import Command, CommandHandler
from django.db import transaction


class UserCreatePostCommand(Command):
    account_id: str
    dto: UserCreatePostDto

    def __init__(self, account_id: str, dto: UserCreatePostDto) -> None:
        self.account_id = account_id
        self.dto = dto


class UserCreatePostCommandHandler(CommandHandler):
    media_service: MediaService

    def __init__(self, media_service: MediaService = MediaServiceImpl()) -> None:
        self.media_service = media_service

    def handle(self, command: UserCreatePostCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        with transaction.atomic():
            post: Post = Post.create_new_post(account, command.dto.content)
            post.save()
            # update media
            self.media_service.create_post_medias(post.id, command.dto.media_datas)

        return super().handle(command)