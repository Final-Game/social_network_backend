from django.db import models
from core.domain.models.base_model import BaseModel


class UserEvent(BaseModel):
    account = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, blank=False, null=False
    )
    event = models.ForeignKey(
        to="Event", on_delete=models.CASCADE, blank=False, null=False
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
