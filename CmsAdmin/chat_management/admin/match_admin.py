from django.contrib import admin
from core.admin.utils import linkify
from chat_management.models import Match


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [linkify("sender"), linkify("receiver"), "status"]
    list_display_links = []

    fields = ["sender", "receiver", "status"]