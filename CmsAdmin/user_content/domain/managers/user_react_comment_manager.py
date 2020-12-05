from django.db.models import Manager, Q
from user_content.domain.exceptions.uc_domain_exception import UcDomainException


class UserReactCommentManager(Manager):
    def find_by_account_and_comment(
        self, account, comment, raise_exception: bool = False
    ):
        condition = Q(sender=account, comment=comment)

        user_react_comment = (
            super(UserReactCommentManager, self)
            .get_queryset()
            .filter(condition)
            .first()
        )

        if not user_react_comment and raise_exception:
            raise UcDomainException(f"Can't find user react comment.")

        return user_react_comment
