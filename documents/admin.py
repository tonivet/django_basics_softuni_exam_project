from django.contrib import admin

from .models import DocumentsModel

# Register your models here.

@admin.register(DocumentsModel)
class DocumentsModelAdmin(admin.ModelAdmin):
    ...
