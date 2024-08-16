from django.contrib import admin
from apps.application.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'passport',
        'pinfl',
        'gender',
        'faculty',
        'birth_date',
    )