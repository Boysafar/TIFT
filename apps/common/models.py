from django.db import models


class Regions(models.Model):
    title = models.CharField(max_length=255)


class Districts(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)



