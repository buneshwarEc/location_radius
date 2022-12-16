# Generated by Django 4.0.1 on 2022-12-12 11:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0003_alter_location_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]