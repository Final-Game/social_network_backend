from django.db import models
from core.domain.models.base_model import BaseModel


class Message(BaseModel):
    room = models.ForeignKey(
        to="Room", on_delete=models.CASCADE, blank=False, null=False
    )
    sender = models.ForeignKey(
        to="UserRoom",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    content = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        db_table = "cm_messages"
    
    def __str__(self) -> str:
        return super().__str__() + f" - {self.content}"
