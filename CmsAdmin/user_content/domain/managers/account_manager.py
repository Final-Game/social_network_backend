from user_content.domain.exceptions.uc_domain_exception import UcDomainException
from django.db.models import Manager, Q


class AccountManager(Manager):
    def find_account_by_id(self, account_id: str, raise_exception: bool = False):
        condition = Q(id=account_id)

        account = super(AccountManager, self).get_queryset().filter(condition).first()
        if not account and raise_exception:
            raise UcDomainException(f"Can't find account with id: {account_id}")
        return account

    def find_account_by_username(self, username: str, raise_exception: bool = False):
        condition = Q(username=username)

        account = super(AccountManager, self).get_queryset().filter(condition).first()

        if not account and raise_exception:
            raise UcDomainException(f"Username {username} not found.")

        return account
