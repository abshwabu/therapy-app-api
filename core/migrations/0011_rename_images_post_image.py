# Generated by Django 4.2.7 on 2024-02-06 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_post_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='images',
            new_name='image',
        ),
    ]