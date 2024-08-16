from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=20)