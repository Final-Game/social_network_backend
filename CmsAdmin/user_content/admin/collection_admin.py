from django.contrib import admin

from core.admin.base_admin import BaseAdmin
from core.admin.utils import linkify

from user_content.models import Collection


@admin.register(Collection)
class CollectionAdmin(BaseAdmin):
    list_display = [linkify("profile")]
    fields = ["profile"]