from django.db import models
from core.domain.models.base_model import BaseModel


class Room(BaseModel):
    general_name = models.CharField(max_length=100, blank=False, null=False)