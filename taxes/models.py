from django.db import models
from django.core.validators import MinValueValidator

from . import choices

# Create your models here.

class MonthlyTax(models.Model):
    building = models.ForeignKey('condominium.Building', on_delete=models.PROTECT)
    renovation_fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    bills_fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    last_update = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.building}"
    
    class Meta:
        verbose_name_plural = 'Monthly Taxes'


class RenovationFundIncome(models.Model):
    date = models.DateField()
    flat_number = models.ForeignKey("condominium.Flat", on_delete=models.PROTECT)
    tax = models.DecimalField(max_digits=6, decimal_places=2)


class RenovationFundExpense(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    documents = models.FileField(null=True, blank=True)


class BillsFeesIncome(models.Model):
    date = models.DateField()
    flat_number = models.ForeignKey("condominium.Flat", on_delete=models.PROTECT)
    tax = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])


class BillsFeesExpense(models.Model):
    date = models.DateField(auto_now_add=True)
    expense_name = models.CharField(max_length=55, choices=choices.BillsFeeChoices, default=choices.BillsFeeChoices.OTHER)
    fee = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    documents = models.FileField(null=True, blank=True)


    