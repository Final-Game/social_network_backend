from django.db import models
from core.domain.models.base_model import BaseModel


class Collection(BaseModel):
    profile = models.OneToOneField(
        to="Profile", on_delete=models.CASCADE, blank=False, null=False
    )

    medias = models.ManyToManyField(
        "media_content.Media",
        through="media_content.MediaCollection",
        through_fields=["collection", "media"],
    )

    class Meta:
        db_table = "uc_collections"
