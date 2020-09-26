from django.contrib import admin

from core.admin.utils import linkify
from core.admin.base_admin import BaseAdmin
from user_content.models import FriendShip


@admin.register(FriendShip)
class FriendShipAdmin(BaseAdmin):
    list_display = [linkify("sender"), linkify("receiver"), "status"]
    fields = ["sender", "receiver", "status"]