from typing import List


class UserStoryMedia(object):
    id: str
    content: str
    media_url: str

    def __init__(self, id: str, content: str, media_url: str) -> None:
        self.content = content
        self.media_url = media_url
        self.id = id

    def to_dict(self):
        return {"content": self.content, "media_url": self.media_url, "id": self.id}


class UserStoryDataDto(object):
    id: str
    name: str
    media_datas: List[UserStoryMedia]

    def __init__(
        self, id: str, name: str, media_datas: List[UserStoryMedia] = None
    ) -> None:
        self.id = id
        self.name = name
        self.media_datas = media_datas or []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "media_datas": list(map(lambda x: x.to_dict(), self.media_datas)),
        }
