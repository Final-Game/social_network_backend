from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin

from media_content.models import MediaPost


@admin.register(MediaPost)
class MediaPostAdmin(BaseAdmin):
    list_display = [linkify("media"), linkify("post")]
    fields = ["media", "post"]