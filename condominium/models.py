from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from . import choices

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=55)
    street = models.CharField(max_length=125)
    created_at = models.DateField(auto_now=True, blank=True)
    number_of_flats = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Citizen(models.Model):
    # add constrain ideal_parts sum can't be higher than 100

    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)
    building = models.ManyToManyField(Building)
    flat_number = models.PositiveSmallIntegerField()
    role = models.CharField(max_length=50, choices=choices.CitizenRole, default=choices.CitizenRole.RESIDENT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Ownership(models.Model):
    # add constrain flat_number field could not be higher than number_of_flats in Building class
    # add constrain ideal_parts sum can't be higher than 100

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_number = models.PositiveSmallIntegerField()
    ideal_parts = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)])
    citizen = models.ForeignKey(Citizen, on_delete=models.PROTECT)
    last_update = models.DateField(auto_now=True)
