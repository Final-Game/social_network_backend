class Pageable(object):
    page: int
    limit: int

    def __init__(self, page: int = 0, limit: int = 10) -> None:
        self.page = page
        self.limit = limit
