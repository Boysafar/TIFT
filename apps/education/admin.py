from django.contrib import admin
from apps.education import models


@admin.register(models.Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'education_type')
    list_editable = ('education_type', 'language', )

    search_fields = ('title', 'body')


@admin.register(models.Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'degree',)
    list_editable = ('degree', )


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number')
    list_editable = ('phone_number', 'full_name')