from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, PlaceImage

import requests


class Command(BaseCommand):
    help = 'Add new place'

    def add_arguments(self, parser):
        parser.add_argument('url', help='URL to download json  with place data')

    def handle(self, *args, **kwargs):
        response = requests.get(kwargs['url'])
        response.raise_for_status()

        place_json = response.json()
        title = place_json['title']
        imgs = place_json['imgs']
        desc_short = place_json['description_short']
        desc_long = place_json['description_long']
        lng, lat = place_json['coordinates'].values()
        place, _ = Place.objects.get_or_create(
            title=title,
            description_short=desc_short,
            description_long=desc_long,
            lat=lat, lng=lng
        )
        for index, img in enumerate(imgs):
            response = requests.get(img)
            response.raise_for_status()

            image_content = ContentFile(response.content)
            place_image_obj = PlaceImage.objects.create(
                place=place,
                order=index
            )

            place_image_obj.image.save(f'{place.pk}-{index}.jpg',
                                       image_content, save=True)
