from user_content.domain.enums.model_status_enum import ModelStatusEnum
from django.db import models
from core.domain.models.base_model import BaseModel


class UserStory(BaseModel):
    account = models.ForeignKey(
        to="Account", on_delete=models.CASCADE, blank=False, null=False
    )
    content = models.CharField(max_length=300, null=True, blank=True)
    media_url = models.CharField(max_length=500, null=True, blank=True)

    status = models.IntegerField(
        blank=False,
        null=False,
        choices=ModelStatusEnum.to_choices(),
        default=int(ModelStatusEnum.ACTIVE),
    )

    viewers = models.ManyToManyField(
        "Account", through="StoryViewer", through_fields=["story", "viewer"], related_name="story_viewers"
    )

    class Meta:
        db_table = "user_content_user_story"
