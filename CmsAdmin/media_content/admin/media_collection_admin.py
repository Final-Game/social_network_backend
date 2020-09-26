from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from media_content.models import MediaCollection


@admin.register(MediaCollection)
class MediaCollectionAdmin(BaseAdmin):
    list_display = [linkify("media"), linkify("collection")]
    fields = ["media", "collection"]