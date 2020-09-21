from django.db import models
from core.domain.models.base_model import BaseModel


class Post(BaseModel):
    own_reaction = models.IntegerField(null=True, blank=True, help_text="User feeling")
    account = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, blank=False, null=False
    )
    content = models.CharField(max_length=500, null=True, blank=True)
    type = models.IntegerField(
        default=1, null=False, blank=False, help_text="type hide from timeline"
    )
    base = models.ForeignKey(
        to="self", on_delete=models.SET_NULL, blank=True, null=True
    )
