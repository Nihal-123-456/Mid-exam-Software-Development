# Generated by Django 4.2.4 on 2023-12-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0009_alter_comment_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
