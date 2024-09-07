from django.db import models
from ckeditor.fields import RichTextField


class LanguageChoices(models.TextChoices):
    UZ = "uz", "Uzbek tili"
    RU = "ru", "Rus tili"
    EN = "en", "Ingiliz tili"


class EducationTypeChoices(models.TextChoices):
    DATA_TAME = "data_tame", "Kundugi"
    PART_TAME = "part_tame", "Sirtqi"
    EVENING = "evening", "Kechgi"


class EducationDegreeChoices(models.TextChoices):
    MASTER = "master", "Magistratura"
    BACHELORS = "bachelors", "Bakalvr"


class Director(models.Model):
    full_name = models.CharField(max_length=255)
    bio = RichTextField()
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return self.full_name


class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    degree = models.CharField(max_length=50, choices=EducationDegreeChoices.choices)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.title


class Direction(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    language = models.CharField(max_length=20, choices=LanguageChoices.choices)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='direction')
    education_type = models.CharField(max_length=20, choices=EducationTypeChoices.choices)

    def __str__(self):
        return self.title




