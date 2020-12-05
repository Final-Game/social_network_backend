from user_content.domain.models.user_comment_post import UserCommentPost
from django.db import transaction

from user_content.app.dtos.comment_dto import CommentDto
from core.app.bus import Command, CommandHandler
from user_content.models import Post, Account


class UserCommentInPostCommand(Command):
    account_id: str
    post_id: str
    dto: CommentDto

    def __init__(self, account_id: str, post_id: str, dto: CommentDto) -> None:
        self.account_id = account_id
        self.post_id = post_id
        self.dto = dto


class UserCommentInPostCommandHandler(CommandHandler):
    def handle(self, command: UserCommentInPostCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        post: Post = Post.objects.find_post_by_id(command.post_id, raise_exception=True)
        self.validate_user_can_comment_in_post(account, post)

        with transaction.atomic():
            user_comment_data: dict = {
                "post": post,
                "content": command.dto.content,
                "sender": account,
            }
            if command.dto.base_id:
                user_comment_data.update({"base_id": command.dto.base_id})

            user_comment_post: UserCommentPost = UserCommentPost.objects.create(
                **user_comment_data
            )

            post.usercommentpost_set.add(user_comment_post)
            post.save()

        return super().handle(command)

    def validate_user_can_comment_in_post(self, account: Account, post: Post):
        return
