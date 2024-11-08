# Generated by Django 5.1.3 on 2024-11-08 11:51

import cloudinary.models
import petstagram_app.photos.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[petstagram_app.photos.validators.FileSizeValidator(5)], verbose_name='image'),
        ),
    ]