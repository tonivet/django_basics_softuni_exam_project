from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from . import choices

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    city = models.CharField(max_length=55)
    street = models.CharField(max_length=125)
    created_at = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

  
class Flat(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_number = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    ideal_parts = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(100), MinValueValidator(0)])
    last_update = models.DateField(auto_now=True)

    # check if ideal_parts of the flats exceed 100% and return error if so 
    def clean(self):
        total = (
            Flat.objects
            .exclude(pk=self.pk)  # important for updates
            .aggregate(sum=Sum("ideal_parts"))["sum"]
            or 0
        )

        if total + self.ideal_parts > 100:
            free = 100 - total
            raise ValidationError({
                "ideal_parts": f"Total allocation cannot exceed 100%. You can add max {free}% ideal parts."
            })

    def __str__(self):
        return f"{self.building} ап. {self.flat_number}"
    
    class Meta:
        unique_together = ['building', 'flat_number']


class FlatResident(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=choices.FlatRole, default=choices.FlatRole.RESIDENT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

