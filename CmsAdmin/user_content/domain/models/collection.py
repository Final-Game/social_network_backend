from typing import List
from django.db import models
from core.domain.models.base_model import BaseModel
from dataclasses import dataclass


@dataclass
class MediaMapper:
    url: str
    type: int


class Collection(BaseModel):
    profile = models.OneToOneField(
        to="Profile", on_delete=models.CASCADE, blank=True, null=True
    )

    medias = models.ManyToManyField(
        "media_content.Media",
        through="media_content.MediaCollection",
        through_fields=["collection", "media"],
    )

    class Meta:
        db_table = "uc_collections"

    def update_medias(self, medias: List[MediaMapper]):
        from media_content.models import Media

        def save_media_map(_m: MediaMapper) -> Media:
            media: Media = Media(url=_m.url, type=_m.type)
            media.save()
            return media

        self.medias.clear()
        self.medias.add(*list(map(lambda x: save_media_map(x), medias)))
