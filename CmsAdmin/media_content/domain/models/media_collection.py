from django.db import models
from core.domain.models.base_model import BaseModel


class MediaCollection(BaseModel):
    media = models.ForeignKey(
        to="Media", on_delete=models.CASCADE, blank=True, null=True
    )
    collection = models.ForeignKey(
        to="user_content.Collection", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        unique_together = ["media", "collection"]
