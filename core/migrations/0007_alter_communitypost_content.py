# Generated by Django 4.2.7 on 2024-01-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_description_communitypost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='content',
            field=models.TextField(),
        ),
    ]
