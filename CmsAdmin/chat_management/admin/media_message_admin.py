from django.contrib import admin
from chat_management.models import MediaMessage

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify


@admin.register(MediaMessage)
class MediaMessageAdmin(BaseAdmin):
    list_display = [linkify("message"), "type"]
    fields = ["message", "media_url", "type"]
