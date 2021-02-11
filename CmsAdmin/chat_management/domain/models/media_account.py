from django.db import models
from core.domain.models.base_model import BaseModel
from chat_management.domain.enums.media_type_enum import MediaTypeEnum


class MediaAccount(BaseModel):
    account = models.ForeignKey(
        "AccountMapper", on_delete=models.CASCADE, blank=False, null=True
    )
    media_url = models.CharField(max_length=300, blank=False, null=False)
    type = models.IntegerField(
        null=True,
        blank=True,
        default=MediaTypeEnum.PHOTO.value,
        choices=MediaTypeEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_media_accounts"
