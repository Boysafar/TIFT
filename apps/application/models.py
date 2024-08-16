from django.db import models
from apps.users.models import User
from apps.common.models import Districts


class Application(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    passport = models.CharField(max_length=255)
    pinfl = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()

    faculty = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport}"
