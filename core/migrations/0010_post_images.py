# Generated by Django 4.2.7 on 2024-02-06 13:15

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(null=True, upload_to=core.models.post_image_file_path),
        ),
    ]