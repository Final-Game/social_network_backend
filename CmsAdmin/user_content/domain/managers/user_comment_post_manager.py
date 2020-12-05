from django.db.models import Manager, Q
from user_content.domain.exceptions.uc_domain_exception import UcDomainException


class UserCommentPostManager(Manager):
    def find_comment_by_id(self, comment_id: str, raise_exception: bool = False):
        condition = Q(id=comment_id)

        comment = (
            super(UserCommentPostManager, self).get_queryset().filter(condition).first()
        )

        if not comment and raise_exception:
            raise UcDomainException(f"Can't find comment with id: {comment_id}")

        return comment
