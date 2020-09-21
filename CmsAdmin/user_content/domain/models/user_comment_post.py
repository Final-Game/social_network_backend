from django.db import models
from core.domain.models.base_model import BaseModel


class UserCommentPost(BaseModel):
    post = models.ForeignKey(
        to="Post", on_delete=models.CASCADE, null=False, blank=False
    )
    content = models.CharField(blank=False, null=False, max_length=500)
    sender = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, null=False, blank=False
    )
    base = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True)
