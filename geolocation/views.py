from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from .models import *
from .serializers import *
# for geodjango postgis
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from .models import *
from django.contrib.gis.geos import GEOSGeometry


def CloseLab():
    print("hello it me")
    lng = -6.67968750000004
    lat = 16.2990510145818
    radius = 10
    point = Point(lng, lat)
    print("lcose", point)
    b = Place.objects.filter(location__distance_lt=(point, D(km=radius)))
    print("b", len(b))


CloseLab()


class locationView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = locationSerializer
    queryset = location.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)


class geolocationView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = locationSerializer
    queryset = location.objects.all()
    lookup_field = 'id'

    lat = 11
    long = 72
    radius = 1
    point = GEOSGeometry('POINT({} {})'.format(long, lat), srid=4326)
    print("point", point)
    int_user_distance = 5
    user_location = Point(float(long), float(lat), srid=4326)
    print(user_location)
    print("user_location", user_location)

    def get_queryset(self):

        a = location.objects.filter(lat_long__distance_lte=(self.user_location, D(km=self.int_user_distance).m)).annotate(
            distance=Distance("lat_long", self.user_location)).order_by("distance")
        print(a)
        print(len(a))
        return location.objects.filter(lat_long__distance_lte=(self.user_location, D(km=self.int_user_distance).m)).annotate(distance=Distance("lat_long", self.user_location)).order_by("distance")

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)


# # create filter for distance for latlong
a = location.objects.filter(lat_long__distance_lte=(point, D(km=radius).m))
a = location.objects.annotate(
    distance=Distance('lat_long', Location.lat_long)
).filter(distance__lte=F('radius'))

lng = -6.67968750000004
lat = 16.2990510145818
radius = 10
point = Point(lng, lat)
print("lcose", point)