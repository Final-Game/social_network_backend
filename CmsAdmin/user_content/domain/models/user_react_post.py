from django.db import models
from core.domain.models.base_model import BaseModel


class UserReactPost(BaseModel):
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, blank=False, null=False
    )
    type = models.IntegerField(blank=False, null=False, help_text="love or live")
    sender = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        db_table = "user_react_post"
