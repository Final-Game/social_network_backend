from django.db import models
from core.domain.models.base_model import BaseModel


class Collection(BaseModel):
    profile = models.ForeignKey(
        to="Profile", on_delete=models.CASCADE, blank=False, null=False
    )
