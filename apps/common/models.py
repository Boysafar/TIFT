from django.db import models


class Regions(models.Model):
    title = models.CharField(max_length=255)
    order_id = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order_id", "id"]
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.title


class Districts(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, related_name='districts')
    order_id = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order_id", "id"]
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.title


class Socials(models.Model):
    class SocialCheeses(models.TextChoices):
        TELEGRAM = "telegram", "Telegram"
        INSTAGRAM = "instagram", "instagram"
        YOUTUBE = "youtube", "Youtube"
        FACEBOOK = "facebook", "Facebook"

    title = models.CharField(max_length=255)
    social = models.CharField(choices=SocialCheeses.choices, max_length=16)
    link = models.URLField()

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"



