class UserStoryDto(object):
    content: str
    media_url: str

    def __init__(self, content: str = "", media_url: str = "") -> None:
        self.content = content
        self.media_url = media_url