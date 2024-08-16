from django.db import models


class Direction(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    language = models.ForeignKey('apps.education.Language', )
    faculty = models.ForeignKey('apps.education.Faculty', on_delete=models.CASCADE)
    education_type = models.ForeignKey('apps.education.EducationType', )


class Language(models.Model):
    title = models.CharField(max_length=255)


class EducationType(models.Model):
    title = models.CharField(max_length=255)


class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    education_degree = models.ForeignKey('apps.education.EducationDegree')
    director = models.ForeignKey('apps.education.Director')


class EducationDegree(models.Model):
    title = models.CharField(max_length=255)


class Director(models.Model):
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)
    picture = models.CharField(max_length=255)