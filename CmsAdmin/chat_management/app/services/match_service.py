from abc import ABC
from chat_management.app.dtos.create_match_dto import CreateMatchDto

from codegen_protos import (
    match_service_pb2 as match_service_pb2,
    match_service_pb2_grpc as match_service_pb2_grpc,
)


class MatchService:
    async def create_match(self, account_id: str, dto: CreateMatchDto):
        raise NotImplementedError()