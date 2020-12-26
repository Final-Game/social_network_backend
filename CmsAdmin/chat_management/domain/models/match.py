from chat_management.domain.enums.match_status_enum import MatchStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class Match(BaseModel):
    sender = models.ForeignKey(
        "user_content.Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="account_sender_related",
    )
    receiver = models.ForeignKey(
        "user_content.Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="account_receiver_related",
    )
    status = models.IntegerField(
        blank=False,
        null=False,
        default=int(MatchStatusEnum.CLOSE),
        choices=MatchStatusEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_matches"
        unique_together = ["sender", "receiver"]
