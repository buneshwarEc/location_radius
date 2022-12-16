from django.contrib import admin
from django.urls import path , include
from .views import *
urlpatterns = [
    path('locationView/', locationView.as_view(), name='locationView'),
    path('locationView/<str:id>/', locationView.as_view(), name='locationView Update'),

    path('geolocationView/', geolocationView.as_view(), name='geolocationView'),
]
