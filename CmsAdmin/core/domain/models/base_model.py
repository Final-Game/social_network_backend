import uuid

from django.db import models


def pkgen():
    return str(uuid.uuid4())


class BaseModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=pkgen)

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

    def __str__(self) -> str:
        return f"{self.__class__.__name__} - {self.short_id}"
