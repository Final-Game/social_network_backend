from CmsAdmin.settings.utils import get_os_env

GRPC_HOST = get_os_env("SN_GRPC_HOST")
GRPC_PORT = get_os_env("SN_GRPC_PORT")