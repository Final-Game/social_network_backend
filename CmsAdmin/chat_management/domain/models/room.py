from chat_management.domain.enums.room_type_enum import RoomTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class Room(BaseModel):
    general_name = models.CharField(max_length=100, blank=False, null=False)
    type = models.IntegerField(
        blank=False,
        null=False,
        default=int(RoomTypeEnum.NORMAL),
        choices=RoomTypeEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_rooms"