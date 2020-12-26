from chat_management.domain.enums.react_room_status_enum import ReactRoomStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class ReactSmartRoom(BaseModel):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, blank=False, null=False)
    sender = models.ForeignKey(
        "UserRoom", on_delete=models.CASCADE, blank=False, null=False
    )
    status = models.IntegerField(
        blank=False,
        null=False,
        default=int(ReactRoomStatusEnum.LOVE),
        choices=ReactRoomStatusEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_react_smart_rooms"
        unique_together = ["room", "sender"]
