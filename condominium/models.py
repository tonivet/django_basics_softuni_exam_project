from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from . import choices

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=55)
    street = models.CharField(max_length=125)
    created_at = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Citizen(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=55, choices=choices.CitizenRole, default=choices.CitizenRole.RESIDENT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

  
class Flat(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_number = models.PositiveSmallIntegerField()
    ideal_parts = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)])
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.building} flat. {self.flat_number}"
    
    class Meta:
        unique_together = ['building', 'flat_number']


class FlatResident(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    citizen = models.ForeignKey(Citizen, on_delete=models.PROTECT)
    role = models.CharField(max_length=50, choices=choices.FlatRole, default=choices.FlatRole.RESIDENT)

    def __str__(self):
        return f"{self.flat} {self.citizen}"

