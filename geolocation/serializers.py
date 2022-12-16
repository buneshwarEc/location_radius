from rest_framework import  serializers
from .models import *
from django.conf import settings



class locationSerializer(serializers.ModelSerializer):

    class Meta:
        model= location
        fields='__all__'


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Place
        fields='__all__'