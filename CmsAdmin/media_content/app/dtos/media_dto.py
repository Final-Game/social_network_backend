class MediaDto(object):
    url: str
    type: str

    def __init__(self, url: str, type: str) -> None:
        self.url = url
        self.type = type

    def to_dict(self):
        return {"url": self.url, "type": self.type}
