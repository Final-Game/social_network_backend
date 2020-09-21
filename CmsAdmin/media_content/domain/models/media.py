from django.db import models
from core.domain.models.base_model import BaseModel


class Media(BaseModel):
    url = models.CharField(null=True, blank=True, max_length=200)
    type = models.IntegerField(null=False, blank=False, help_text="1- video, 0- photo")