# Generated by Django 4.2.4 on 2023-12-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
