from django.db import models
from core.domain.models.base_model import BaseModel


class Connection(BaseModel):
    google_token = models.CharField(blank=True, null=True, max_length=100)
    microsoft_token = models.CharField(blank=True, null=True, max_length=100)