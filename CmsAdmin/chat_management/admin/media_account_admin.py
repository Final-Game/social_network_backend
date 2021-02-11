from django.contrib import admin
from django.utils.html import format_html


from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from chat_management.models import MediaAccount


@admin.register(MediaAccount)
class MediaAccountAdmin(BaseAdmin):
    list_display = [linkify("account"), "media_image", "type"]
    fields = ["account", "media_url", "type"]

    def media_image(self, obj):
        return format_html(
            '<img src="{0}" style="width: 45px; height:45px;" />'.format(obj.media_url)
        )
