# Generated by Django 5.1 on 2024-08-27 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_publish_tame_news_publish_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'NewsContent', 'verbose_name_plural': 'NewsContents'},
        ),
    ]
