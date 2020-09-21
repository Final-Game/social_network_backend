from django.db import models
from core.domain.models.base_model import BaseModel


class UserRoom(BaseModel):
    room = models.ForeignKey(
        to="Room", on_delete=models.CASCADE, null=False, blank=False
    )
    account = models.ForeignKey(
        to="user_content.Account", on_delete=models.CASCADE, blank=False, null=False
    )
    nick_name = models.CharField(blank=False, null=False, max_length=36)
