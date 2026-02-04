from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.MonthlyTax)
class MonthlyTaxAdmin(admin.ModelAdmin):
    list_display = ['building', 'renovation_fee', 'bills_fee']

@admin.register(models.RenovationFundIncome)
class RenovationFundIncomeAdmin(admin.ModelAdmin):
    ...
