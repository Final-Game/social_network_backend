from typing import List


class MediaPostData(object):
    url: str
    type: int  # 1 - video, 0 - photo

    def __init__(self, url: str, type: int = 0) -> None:
        self.url = url
        self.type = type


class UserCreatePostDto(object):
    content: str
    media_datas: List[MediaPostData]

    def __init__(self, content: str, media_datas: List[MediaPostData] = None) -> None:
        self.content = content
        self.media_datas = media_datas or []
