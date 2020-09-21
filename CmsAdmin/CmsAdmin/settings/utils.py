import os


def get_os_env(name, default=None, assert_exist=True):
    if name in os.environ:
        value = os.environ[name]
        if value.upper() in ["TRUE", "FALSE"]:
            return value.upper() == "TRUE"
        return os.environ[name]
    return default
