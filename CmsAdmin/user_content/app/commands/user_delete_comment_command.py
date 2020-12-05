from django.db import transaction
from core.common.base_api_exception import BaseApiException
from user_content.domain.models.post import Post
from user_content.domain.models.user_comment_post import UserCommentPost
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler


class UserDeleteCommentCommand(Command):
    account_id: str
    comment_id: str

    def __init__(self, account_id: str, comment_id: str) -> None:
        self.account_id = account_id
        self.comment_id = comment_id


class UserDeleteCommentCommandHandler(CommandHandler):
    def handle(self, command: UserDeleteCommentCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        comment: UserCommentPost = UserCommentPost.objects.find_comment_by_id(
            command.comment_id, raise_exception=True
        )
        self.validate_user_can_remove_comment(account, comment)

        comment.delete()
        return True

    def validate_user_can_remove_comment(
        self, account: Account, comment: UserCommentPost
    ):
        base_post: Post = comment.post
        base_account: Account = base_post.account

        owner_comment: Account = comment.sender

        if account not in [base_account, owner_comment]:
            raise BaseApiException("Account can't delete comment.")
