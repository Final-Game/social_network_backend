from abc import ABC
import grpc
from grpc import Channel

from django.conf import settings


class GrpcService(ABC):
    host: str
    port: int

    def __init__(
        self, host: str = settings.GRPC_HOST, port: int = settings.GRPC_PORT
    ) -> None:
        self.host = host
        self.port = port

    def get_connection(self) -> Channel:
        return grpc.aio.insecure_channel(f"{self.host}:{self.port}")
