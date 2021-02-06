from user_content.domain.enums.verify_status_enum import VerifyStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class AccountVerify(BaseModel):
    account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, blank=False, null=False
    )
    front_photo_url = models.TextField(blank=True, null=True)
    back_photo_url = models.TextField(blank=True, null=True)
    status = models.IntegerField(
        blank=True,
        null=True,
        default=VerifyStatusEnum.PENDING.value,
        choices=VerifyStatusEnum.to_choices(),
    )

    class Meta:
        db_table = "uc_account_virifies"
