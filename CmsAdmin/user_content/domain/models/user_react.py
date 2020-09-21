from django.db import models
from core.domain.models.base_model import BaseModel


class UserReact(BaseModel):
    target_react_id = models.UUIDField(
        blank=False,
        null=False,
    )
    type = models.IntegerField(blank=False, null=False, help_text="love or live")
    sender = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, null=False, blank=False
    )
