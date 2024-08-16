from django.db import models


class Districts(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey('apps.common.Regions', on_delete=models.CASCADE)


class Regions(models.Model):
    title = models.CharField(max_length=255)

