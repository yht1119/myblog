# Generated by Django 5.0.1 on 2025-04-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="myuser",
            name="background_image",
            field=models.ImageField(
                blank=True, upload_to="backgrounds/", verbose_name="背景图像"
            ),
        ),
    ]
