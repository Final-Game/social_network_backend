class CommentDto(object):
    content: str
    base_id: str

    def __init__(self, content: str, base_id: str = None) -> None:
        self.base_id = base_id
        self.content = content
