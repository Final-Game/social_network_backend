from core.common.base_api_exception import BaseApiException
from user_content.domain.models.post import Post
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler


class UserDeletePostCommand(Command):
    account_id: str
    post_id: str

    def __init__(self, account_id: str, post_id: str) -> None:
        self.account_id = account_id
        self.post_id = post_id


class UserDeletePostCommandHandler(CommandHandler):
    def handle(self, command: UserDeletePostCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        post: Post = Post.objects.find_post_by_id(command.post_id, raise_exception=True)

        self.validate_user_can_remove_post(account, post)
        post.delete()

        return True

    def validate_user_can_remove_post(self, account: Account, post: Post):
        owner: Account = post.account

        if account != owner:
            raise BaseApiException("Account can't remove this post.")