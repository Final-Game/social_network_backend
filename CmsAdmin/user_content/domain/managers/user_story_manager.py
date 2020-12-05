from user_content.domain.exceptions.uc_domain_exception import UcDomainException
from django.db.models import Manager, Q


class UserStoryManager(Manager):
    def find_story_by_id(self, story_id: str, raise_exception: bool = False):
        condition = Q(id=story_id)

        story = super(UserStoryManager, self).get_queryset().filter(condition).first()
        if not story and raise_exception:
            raise UcDomainException(f"Can't find story with id: {story_id}")

        return story