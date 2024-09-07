from django.contrib import admin
from apps.common import models


@admin.register(models.Regions)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order_id')
    list_editable = ('order_id', )


@admin.register(models.Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'region', 'order_id')
    list_editable = ('order_id', )


@admin.register(models.Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'social', 'link')
    list_editable = ('title', 'social', 'link')




