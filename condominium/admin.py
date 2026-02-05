from django.contrib import admin

from . import models
# Register your models here.

@admin.register(models.Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'street']
    search_fields = ['name']


@admin.register(models.Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ['building', 'floor', 'flat_number', 'ideal_parts']


@admin.register(models.FlatResident)
class FlatResidentsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'role', 'flat']




