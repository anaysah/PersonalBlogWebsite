# Generated by Django 4.1.7 on 2023-07-30 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_image_public_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]
