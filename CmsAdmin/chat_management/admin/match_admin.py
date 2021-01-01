from django.contrib import admin
from core.admin.utils import linkify
from chat_management.models import Match
from core.admin.base_admin import BaseAdmin


@admin.register(Match)
class MatchAdmin(BaseAdmin):
    list_display = [linkify("sender"), linkify("receiver"), "status"]
    list_display_links = []

    fields = ["sender", "receiver", "status"]
