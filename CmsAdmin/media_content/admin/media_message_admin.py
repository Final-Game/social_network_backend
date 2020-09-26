from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from media_content.models import MediaMessage


@admin.register(MediaMessage)
class MediaMessageAdmin(BaseAdmin):
    list_display = [linkify("media"), linkify("message")]
    fields = ["media", "message"]