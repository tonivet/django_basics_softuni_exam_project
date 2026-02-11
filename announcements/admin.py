from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['author']
    list_display = ['title', 'author', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status']
