from django.db import models
from core.domain.models.base_model import BaseModel


class Account(BaseModel):
    username = models.CharField(blank=False, null=False, max_length=50, unique=True)
    password = models.CharField(blank=False, null=False, max_length=250)
    connection = models.OneToOneField(
        to="Connection", on_delete=models.SET_NULL, blank=True, null=True
    )
    profile = models.OneToOneField(
        to="Profile", on_delete=models.SET_NULL, blank=True, null=True
    )
