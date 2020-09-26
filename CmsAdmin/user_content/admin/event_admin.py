from django.contrib import admin
from core.admin.base_admin import BaseAdmin

from user_content.models import Event


@admin.register(Event)
class EventAdmin(BaseAdmin):
    list_display = ["name", "type"]
    list_display_links = ["name"]
    fields = ["name", "type"]