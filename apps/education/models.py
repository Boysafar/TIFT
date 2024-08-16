from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=255)


class EducationType(models.Model):
    title = models.CharField(max_length=255)


class EducationDegree(models.Model):
    title = models.CharField(max_length=255)


class Director(models.Model):
    bio = models.TextField()
    phone_number = models.CharField(max_length=20)
    picture = models.CharField(max_length=255)


class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    education_degree = models.ForeignKey(EducationDegree, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Direction(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    education_type = models.ForeignKey(EducationType, on_delete=models.CASCADE)




