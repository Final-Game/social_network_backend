import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        abstract = True

    @property
    def short_id(self) -> str:
        try:
            id_string: str = str(self.id)
        except:
            return ""

        return id_string[:8]
