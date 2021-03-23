from django.contrib import admin
from . import models

# Register your models here.


class PostChangeViewOrder(admin.ModelAdmin):
    # fields = ['author', 'title', 'content']
    fieldsets = [
        ('data', {'fields': ['author', 'title', 'content']}),
        ('date info', {'fields': ['date_create']}),
    ]

    list_display = ('title', 'author', 'date_create', 'date_update')

    list_filter = ['title', 'author', 'date_create']

    search_fields = ['title']


admin.site.register(models.Post, PostChangeViewOrder)
