from django.shortcuts import render

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
                                  "detailsUrl": "1"
                              }
                          } for place in places
                      ]
                  }}
                  )