from django.db import models
from core.domain.models.base_model import BaseModel


class Message(BaseModel):
    room = models.ForeignKey(
        to="Room", on_delete=models.CASCADE, blank=False, null=False
    )
    sender = models.ForeignKey(
        to="user_content.Account", on_delete=models.CASCADE, blank=False, null=False
    )
    content = models.CharField(blank=True, null=True, max_length=200)
