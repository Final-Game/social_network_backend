from django.db import models
from core.domain.models.base_model import BaseModel


class MediaMessage(BaseModel):
    media = models.ForeignKey(
        to="Media", on_delete=models.CASCADE, blank=True, null=True
    )
    message = models.ForeignKey(
        to="chat_management.Message", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        unique_together = ["media", "message"]
