from user_content.domain.managers.user_react_comment_manager import (
    UserReactCommentManager,
)
from user_content.domain.enums.react_type_enum import ReactTypeEnum

from django.db import models
from core.domain.models.base_model import BaseModel


class UserReactComment(BaseModel):
    comment = models.ForeignKey(
        "UserCommentPost", on_delete=models.CASCADE, null=False, blank=False
    )
    sender = models.ForeignKey(
        "Account", on_delete=models.CASCADE, null=False, blank=False
    )
    type = models.IntegerField(
        blank=False,
        null=False,
        help_text="love or like",
        choices=ReactTypeEnum.to_choices(),
        default=int(ReactTypeEnum.LIKE),
    )

    objects: UserReactCommentManager = UserReactCommentManager()

    class Meta:
        db_table = "user_react_comment"
        unique_together = ["comment", "sender"]

    def change_react_type(self, type: str):
        self.type = ReactTypeEnum.from_value(type)
