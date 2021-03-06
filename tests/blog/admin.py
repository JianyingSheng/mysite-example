from django.contrib import admin
from . import models
# Register your models here.
# Register the `Post` model

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'status',
        'created',
        'updated',
    )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = (
        'status',
        'topics',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

admin.site.register(models.Post, PostAdmin)

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
