from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from media_content.models import Media


@admin.register(Media)
class MediaAdmin(BaseAdmin):
    list_display = ["url", "type"]
    fields = ["url", "type"]