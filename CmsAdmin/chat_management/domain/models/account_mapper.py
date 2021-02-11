from chat_management.domain.enums.gender_type_enum import GenderTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class AccountMapper(BaseModel):
    ref = models.OneToOneField(
        "user_content.Account",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="chat_ref_account",
    )

    avatar = models.CharField(blank=True, null=True, max_length=300)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.CharField(blank=True, null=True, max_length=256)
    address = models.CharField(blank=True, null=True, max_length=256)
    job = models.CharField(blank=True, null=True, max_length=256)
    reason = models.CharField(blank=True, null=True, max_length=256)
    gender = models.IntegerField(
        blank=True, null=True, choices=GenderTypeEnum.to_choices()
    )
    full_name = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        db_table = "cm_account_mappers"
