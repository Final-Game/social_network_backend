from django.db import models

from core.domain.models.base_model import BaseModel


class Profile(BaseModel):
    avatar = models.CharField(
        blank=True, null=True, max_length=200, help_text="Avatar url"
    )
    cover = models.CharField(
        blank=True, null=True, max_length=200, help_text="Cover url"
    )
    email = models.CharField(blank=True, null=True, max_length=30)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    first_name = models.CharField(blank=True, null=True, max_length=15)
    last_name = models.CharField(blank=True, null=True, max_length=15)
    gender = models.BooleanField(blank=True, null=True)

    marital_status = models.IntegerField(
        blank=True, null=True, help_text="Marital status: 0 - Single, 1 - Got married"
    )
    birth_date = models.DateField(blank=True, null=True)
    school = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    bio = models.CharField(blank=True, null=True, max_length=500)

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}"
