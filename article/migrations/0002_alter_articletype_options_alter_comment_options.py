# Generated by Django 5.0.1 on 2024-11-29 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletype',
            options={'verbose_name': '博客类别管理'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论管理'},
        ),
    ]
