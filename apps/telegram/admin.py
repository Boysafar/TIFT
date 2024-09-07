from django.contrib import admin
from apps.telegram import models


@admin.register(models.Telegram)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'last_name', 'first_name', 'user')
    search_fields = ('user__first_name',)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
