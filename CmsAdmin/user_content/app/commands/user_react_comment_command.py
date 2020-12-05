from user_content.domain.enums.react_type_enum import ReactTypeEnum
from user_content.domain.models.user_react_comment import UserReactComment
from django.db import transaction
from django.db.models import Q

from user_content.domain.models.user_comment_post import UserCommentPost
from user_content.domain.models.account import Account
from user_content.app.dtos.user_react_comment_dto import UserReactCommentDto
from core.app.bus import Command, CommandHandler


class UserReactCommentCommand(Command):
    account_id: str
    comment_id: str

    dto: UserReactCommentDto

    def __init__(
        self, account_id: str, comment_id: str, dto: UserReactCommentDto
    ) -> None:
        self.account_id = account_id
        self.comment_id = comment_id
        self.dto = dto


class UserReactCommentCommandHandler(CommandHandler):
    def handle(self, command: UserReactCommentCommand):
        account: Account = Account.objects.find_account_by_id(
            command.account_id, raise_exception=True
        )
        comment: UserCommentPost = UserCommentPost.objects.find_comment_by_id(
            command.comment_id, raise_exception=True
        )

        self.validate_user_can_react_comment(account, comment)

        with transaction.atomic():
            user_react_comment: UserReactComment = (
                UserReactComment.objects.find_by_account_and_comment(account, comment)
            )
            if not user_react_comment:
                user_react_comment_data: dict = {
                    "sender": account,
                    "comment": comment,
                    "type": ReactTypeEnum.from_value(command.dto.type),
                }

                UserReactComment.objects.create(**user_react_comment_data)
            else:
                user_react_comment.change_react_type(command.dto.type)
                user_react_comment.save()

        return True

    def validate_user_can_react_comment(
        self, account: Account, comment: UserCommentPost
    ):
        return