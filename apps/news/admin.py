from django.contrib import admin
from apps.news import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published', 'publish_time', )
    list_editable = ('is_published', 'publish_time', )

    list_filter = ('is_published', )

    exclude = ('slug', )

    search_fields = ('title', 'body')