from user_content.domain.enums.marital_status_enum import MaritalStatusEnum
from user_content.domain.enums.account_gender_enum import AccountGenderEnum
from django.db import models

from core.domain.models.base_model import BaseModel


class Profile(BaseModel):
    avatar = models.CharField(
        blank=True, null=True, max_length=200, help_text="Avatar url"
    )
    cover = models.CharField(
        blank=True, null=True, max_length=200, help_text="Cover url"
    )
    email = models.CharField(blank=True, null=True, max_length=30, unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    first_name = models.CharField(blank=True, null=True, max_length=15)
    last_name = models.CharField(blank=True, null=True, max_length=15)
    gender = models.IntegerField(
        blank=True,
        null=True,
        choices=AccountGenderEnum.to_choices(),
    )

    marital_status = models.IntegerField(
        blank=True,
        null=True,
        help_text="Marital status: 0 - Single, 1 - Got married",
        choices=MaritalStatusEnum.to_choices(),
    )
    birth_date = models.DateField(blank=True, null=True)
    school = models.CharField(blank=True, null=True, max_length=200)
    address = models.CharField(blank=True, null=True, max_length=200)
    bio = models.CharField(blank=True, null=True, max_length=500)

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}"
