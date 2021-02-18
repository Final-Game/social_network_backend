from user_content.app.commands.report_user_command import ReportUserCommand
from user_content.api.serializers.account_report_request_serializer import (
    AccountReportRequestSerializer,
)
from user_content.app.dtos.report_user_dto import ReportUserDto
from rest_framework.decorators import api_view

from core.api import response
from core.app.bus import Bus

_bus: Bus = Bus()


@api_view(["POST"])
def account_report_api(request, *args, **kwargs):
    account_id: str = kwargs["account_id"]

    if request.method == "POST":
        request_data = AccountReportRequestSerializer(data=request.data)
        request_data.is_valid(raise_exception=True)

        account_report_dto: ReportUserDto = request_data.save()
        _bus.dispatch(ReportUserCommand(account_id, account_report_dto))

        return response.success({"status": "Success"})
