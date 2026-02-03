from django.db import models
from django.core.validators import MinValueValidator

from . import choices

# Create your models here.

class MonthlyTaxes(models.Model):
    bills_fee = models.PositiveSmallIntegerField()
    renovation_fee = models.PositiveSmallIntegerField()
    building = models.ForeignKey('condominium.Building', on_delete=models.PROTECT)
    last_update = models.DateField(auto_now=True, blank=True)

class RenovationFundIncomes(models.Model):
    date = models.DateField()
    flat_number = models.ForeignKey("condominium.Ownership", on_delete=models.PROTECT)
    tax = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

class RenovationFundExpenses(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    documents = models.FileField(null=True, blank=True)

class BillsFeesIncomes(models.Model):
    date = models.DateField()
    flat_number = models.ForeignKey("condominium.Ownership", on_delete=models.PROTECT)
    tax = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

class BillsFeesExpenses(models.Model):
    date = models.DateField(auto_now_add=True)
    expense_name = models.CharField(max_length=55, choices=choices.BillsFeeChoices, default=choices.BillsFeeChoices.OTHER)
    fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    documents = models.FileField(null=True, blank=True)


    
