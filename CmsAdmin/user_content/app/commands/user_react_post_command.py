from user_content.domain.enums.react_type_enum import ReactTypeEnum
from user_content.domain.models.user_react_post import UserReactPost
from django.db import transaction
from django.db.models import Q


from user_content.domain.models.post import Post
from user_content.domain.models.account import Account
from user_content.app.dtos.user_react_post_dto import UserReactPostDto
from core.app.bus import Command, CommandHandler


class UserReactPostCommand(Command):
    account_id: str
    post_id: str

    dto: UserReactPostDto

    def __init__(self, account_id: str, post_id: str, dto: UserReactPostDto) -> None:
        self.account_id = account_id
        self.post_id = post_id
        self.dto = dto


class UserReactPostCommandHandler(CommandHandler):
    def handle(self, command: UserReactPostCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        post: Post = Post.objects.find_post_by_id(command.post_id, raise_exception=True)
        self.validate_user_can_react_post(account, post)

        with transaction.atomic():
            user_react_post: UserReactPost = (
                UserReactPost.objects.filter(Q(post=post) & Q(sender=account)).first()
                or None
            )
            if not user_react_post:
                user_react_post_data: dict = {
                    "post": post,
                    "sender": account,
                    "type": ReactTypeEnum.from_value(command.dto.type),
                }

                UserReactPost.objects.create(**user_react_post_data)
            else:
                user_react_post.change_react_type(command.dto.type)
                user_react_post.save()

        return True

    def validate_user_can_react_post(self, account: Account, post: Post):
        return