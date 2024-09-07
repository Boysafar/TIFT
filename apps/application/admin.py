from django.contrib import admin
from apps.application.models import Application, ApplicationStatusChoices


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', "last_name", 'passport', 'status',)
    list_editable = ('status', )
