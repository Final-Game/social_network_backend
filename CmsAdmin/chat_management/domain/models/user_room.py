from django.db import models
from core.domain.models.base_model import BaseModel


class UserRoom(BaseModel):
    room = models.ForeignKey(to="Room", on_delete=models.CASCADE, null=True, blank=True)
    account = models.ForeignKey(
        to="AccountMapper", on_delete=models.CASCADE, blank=True, null=True
    )
    nick_name = models.CharField(blank=False, null=False, max_length=36)

    class Meta:
        db_table = "cm_user_rooms"
