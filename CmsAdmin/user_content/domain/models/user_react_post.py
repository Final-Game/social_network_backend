from user_content.domain.enums.react_type_enum import ReactTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class UserReactPost(BaseModel):
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, blank=False, null=False
    )
    type = models.IntegerField(
        blank=False,
        null=False,
        help_text="love or haha",
        choices=ReactTypeEnum.to_choices(),
        default=ReactTypeEnum.LIKE,
    )
    sender = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "user_react_post"
        unique_together = ["post", "sender"]

    def change_react_type(self, type: str):
        self.type = ReactTypeEnum.from_value(type)
