from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from chat_management.models import Room


@admin.register(Room)
class RoomAdmin(BaseAdmin):
    list_display = ["general_name"]
    list_display_links = ["general_name"]

    fields = ["general_name"]