# Generated by Django 4.1.7 on 2025-01-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_remove_websitesettings_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesettings',
            name='social_media_links',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
