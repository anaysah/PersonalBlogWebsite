# Generated by Django 4.1.7 on 2023-03-22 15:37

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.path_and_rename.wrapper),
        ),
    ]
