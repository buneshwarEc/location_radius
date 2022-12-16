
from django.db import models
from django.contrib.gis.db import models as gismodel
from django.db.models import Manager as GeoManager
# Create your models here.
class location(models.Model):
    lat_long = gismodel.PointField(srid=4326,blank=True,null=True)
    lab_name = models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)



class Place(models.Model):
    id = models.IntegerField(primary_key=True)
    location = gismodel.PointField(null=True, blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    objects = GeoManager()

    def __str__(self):
        return str(self.id)