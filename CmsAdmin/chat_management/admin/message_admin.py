from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from chat_management.models import Message


@admin.register(Message)
class MessageAdmin(BaseAdmin):
    list_display = [linkify("room"), linkify("sender"), "content"]
    fields = ["room", "sender", "content"]