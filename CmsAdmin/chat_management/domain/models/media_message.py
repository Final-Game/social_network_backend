from chat_management.domain.enums.media_type_enum import MediaTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class MediaMessage(BaseModel):
    message = models.ForeignKey(
        "Message",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="message_related",
    )
    media_url = models.CharField(max_length=300, blank=False, null=False)
    type = models.IntegerField(
        null=True,
        blank=True,
        default=int(MediaTypeEnum.PHOTO),
        choices=MediaTypeEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_media_messages"
