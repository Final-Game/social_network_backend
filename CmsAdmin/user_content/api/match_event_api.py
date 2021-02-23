from user_content.app.commands.user_match_event_command import UserMatchEventCommand
from rest_framework.decorators import api_view

from core.api import response
from core.app.bus import Bus

__bus: Bus = Bus()


@api_view(["POST"])
def match_event_api(request, *args, **kwargs):
    if request.method == "POST":
        partner_id = request.data.get("partner_id", "")
        account_id = request.data.get("account_id", "")

        __bus.dispatch(UserMatchEventCommand(account_id, partner_id))