# Generated by Django 5.1 on 2024-08-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='telegram',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
