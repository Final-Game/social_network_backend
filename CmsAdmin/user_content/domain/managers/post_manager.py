from user_content.domain.exceptions.uc_domain_exception import UcDomainException
from django.db.models import Manager, Q


class PostManager(Manager):
    def find_post_by_id(self, post_id: str, raise_exception: bool = False):
        condition = Q(id=post_id)

        post = super(PostManager, self).get_queryset().filter(condition).first()
        if not post and raise_exception:
            raise UcDomainException(f"Can't find post with id: {post_id}")

        return post
