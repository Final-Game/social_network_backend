from typing import Iterable, Optional
from django.db import models

from core.domain.models.base_model import BaseModel


class FriendShip(BaseModel):
    sender = models.ForeignKey(
        to="Account",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="sender_friendship",
    )
    receiver = models.ForeignKey(
        to="Account",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="receiver_friendship",
    )
    status = models.IntegerField(
        null=False, blank=False, default=0, help_text="0 - PENDING, 1 - SUCCESS"
    )

    class Meta:
        unique_together = ["sender", "receiver"]
