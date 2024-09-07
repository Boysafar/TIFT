from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import Districts
from apps.education.models import Direction
from datetime import datetime
from django.urls import reverse

User = get_user_model()


class ApplicationStatusChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"


class GENDER_CHOICES(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    passport = models.CharField(max_length=9)
    pinfl = models.CharField(max_length=14)
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES)
    birth_date = models.DateField()

    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=16, choices=ApplicationStatusChoices.choices)
    district = models.ForeignKey(Districts, on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.DateTimeField(null=True, blank=True)
    contract_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.passport}"

    def save(self, *args, **kwargs):
        from weasyprint import HTML
        from django.conf import settings
        import os
        super().save(*args, **kwargs)

        if (self.status == ApplicationStatusChoices.ACCEPTED or self.status == ApplicationStatusChoices.REJECTED) and not self.accepted:

            if self.status == ApplicationStatusChoices.ACCEPTED:
                if not os.path.exists('contracts'):
                    os.makedirs('contracts')

                file_name = f"contracts/{self.first_name}-{self.last_name}.pdf"
                try:
                    url = f"{settings.HOST_NAME}{reverse('application-generator')}?application_id={self.pk}"
                    print(f"Generated URL: {url}")
                    HTML(url).write_pdf(file_name)
                    self.contract_url = file_name

                except Exception as e:
                    print(f"Error generating PDF: {e}")

            self.accepted = datetime.now()
            super().save(update_fields=['accepted', 'contract_url'])
