# Generated by Django 4.2.7 on 2024-01-31 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_communitypost_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommunityPost',
            new_name='Post',
        ),
    ]