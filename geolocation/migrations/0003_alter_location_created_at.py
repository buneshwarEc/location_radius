# Generated by Django 4.0.1 on 2022-12-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocation', '0002_location_lab_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]