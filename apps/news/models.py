from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.CharField(max_length=255)


class Socials(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(null=True, blank=True)