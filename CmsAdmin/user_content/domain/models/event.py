from django.db import models
from core.domain.models.base_model import BaseModel


class Event(BaseModel):
    name = models.CharField(blank=False, null=False, max_length=100)
    type = models.IntegerField(blank=False, null=False, help_text="type of event")