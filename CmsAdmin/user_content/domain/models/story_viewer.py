from user_content.domain.enums.react_type_enum import ReactTypeEnum
from django.db import models
from django.db.models.deletion import CASCADE
from core.domain.models.base_model import BaseModel


class StoryViewer(BaseModel):
    story = models.ForeignKey("UserStory", on_delete=CASCADE, blank=False, null=False)
    viewer = models.ForeignKey(
        "Account", on_delete=models.CASCADE, blank=False, null=False
    )
    react_type = models.IntegerField(
        null=True, blank=True, choices=ReactTypeEnum.to_choices()
    )

    class Meta:
        db_table = "user_content_story_viewer"
        unique_together = ["story", "viewer"]
