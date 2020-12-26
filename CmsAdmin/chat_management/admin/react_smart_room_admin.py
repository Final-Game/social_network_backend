from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from chat_management.models import ReactSmartRoom


@admin.register(ReactSmartRoom)
class ReactSmartRoomAdmin(BaseAdmin):
    list_display = [linkify("room"), linkify("sender"), "status"]
    list_display_links = []

    fields = ["room", "sender", "status"]