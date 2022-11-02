from django.contrib import admin

from news.models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    list_filter = ('date_create',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(NewsModel, NewsAdmin)