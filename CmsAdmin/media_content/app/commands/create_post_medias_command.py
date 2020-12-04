from media_content.domain.models.media_post import MediaPost
from typing import List
from django.db import transaction

from media_content.domain.models.media import Media
from media_content.app.dtos.create_media_list_dto import CreatePostMediaListDto
from media_content.app.dtos.media_dto import MediaDto
from core.app.bus import Command, CommandHandler


class CreatePostMediasCommand(Command):
    dto: CreatePostMediaListDto

    def __init__(self, dto: CreatePostMediaListDto) -> None:
        self.dto = dto


class CreatePostMediasCommandHandler(CommandHandler):
    def handle(self, command: CreatePostMediasCommand):
        post_id: str = command.dto.post_id

        new_media_post_list: List[MediaPost] = []
        with transaction.atomic():
            for media_data in command.dto.medias:
                media: Media = Media.objects.create(**media_data.to_dict())

                new_media_post_list.append(MediaPost(media=media, post_id=post_id))

            MediaPost.objects.bulk_create(new_media_post_list)