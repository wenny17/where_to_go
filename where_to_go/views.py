from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def start_page(request):
    places = Place.objects.all()

    return render(request, "index.html",
                  {'places': {
                      "type": "FeatureCollection",
                      "features": [
                          {
                              "type": "Feature",
                              "geometry": {
                                  "type": "Point",
                                  "coordinates": [place.lng, place.lat]
                              },
                              "properties": {
                                  "title": place.title,
                                  "placeId": place.id,
                                  "detailsUrl": reverse('place_detail', args=(place.pk,))
                              }
                          } for place in places
                      ]
                  }}
                  )
