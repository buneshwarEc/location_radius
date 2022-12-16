from django.contrib import admin
from .models import  *
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
#create github
class locationadmin(admin.ModelAdmin):
    list_display = ['lat_long','lab_name']

admin.site.register(location,locationadmin)

admin.site.register(Place)
