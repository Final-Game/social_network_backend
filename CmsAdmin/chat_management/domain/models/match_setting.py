from chat_management.domain.enums.gender_type_enum import GenderTypeEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class MatchSetting(BaseModel):
    account = models.OneToOneField(
        "user_content.Account", on_delete=models.CASCADE, null=False, blank=False
    )

    max_distance = models.IntegerField(
        null=True, blank=True, default=10, help_text="Max distance in km"
    )
    min_age = models.IntegerField(
        null=True, blank=True, default=18, help_text="Min age"
    )

    max_age = models.IntegerField(
        null=True, blank=True, default=21, help_text="Max age"
    )
    target_gender = models.IntegerField(
        null=True,
        blank=True,
        default=int(GenderTypeEnum.MALE),
        choices=GenderTypeEnum.to_choices(),
    )

    class Meta:
        db_table = "cm_match_settings"
