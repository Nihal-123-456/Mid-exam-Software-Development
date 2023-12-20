# Generated by Django 4.2.4 on 2023-12-19 11:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0003_alter_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]