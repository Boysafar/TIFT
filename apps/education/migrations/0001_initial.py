# Generated by Django 5.1 on 2024-08-19 11:46

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('bio', ckeditor.fields.RichTextField()),
                ('phone_number', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('degree', models.CharField(choices=[('master', 'Magistratura'), ('bachelors', 'Bakalvr')], max_length=50)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.director')),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('language', models.CharField(choices=[('uz', 'Uzbek tili'), ('ru', 'Rus tili'), ('en', 'Ingiliz tili')], max_length=20)),
                ('education_type', models.CharField(choices=[('data_tame', 'Kundugi'), ('part_tame', 'Sirtqi'), ('evening', 'Kechgi')], max_length=20)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.faculty')),
            ],
        ),
    ]
