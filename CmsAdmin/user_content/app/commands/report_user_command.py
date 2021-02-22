from core.common.base_api_exception import BaseApiException
from user_content.domain.models.account_report import AccountReport
from user_content.domain.models.post import Post
from user_content.app.dtos.report_user_dto import ReportUserDto
from user_content.domain.models.account import Account
from core.app.bus import Command, CommandHandler
from django.db import transaction


class ReportUserCommand(Command):
    account_id: str
    dto: ReportUserDto

    def __init__(self, account_id: str, dto: ReportUserDto) -> None:
        self.account_id = account_id
        self.dto = dto


class ReportUserCommandHandler(CommandHandler):
    def handle(self, command: ReportUserCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        receiver: Account = Account.objects.find_account_by_id(
            command.dto.receiver_id, raise_exception=True
        )
        _data: dict = {
            "sender": account,
            "receiver": receiver,
            "reason": command.dto.reason,
        }

        related_post: Post = None
        if command.dto.related_post_id:
            related_post = Post.objects.find_post_by_id(
                command.dto.related_post_id, raise_exception=True
            )
            _data.update({"related_post": related_post})

        self.validate_account_can_report_receiver(account, receiver, related_post)

        with transaction.atomic():
            account.un_follow(receiver)
            AccountReport.objects.create(**_data)

    def validate_account_can_report_receiver(
        self, account: Account, receiver: Account, related_post: Post
    ):
        if account.id == receiver.id:
            raise BaseApiException(f"Can't report own account.")

        if related_post and related_post not in receiver.post_set.all():
            raise BaseApiException(
                f"account {receiver.id} don't have post {related_post.id}"
            )
