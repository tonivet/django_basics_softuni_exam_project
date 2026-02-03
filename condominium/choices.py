from django.db.models import TextChoices

class CitizenRole(TextChoices):
    OWNER = 'Owner', 'owner'
    RESIDENT = 'Resident', 'resident'
    TENANT = 'Tenant', 'tenant'
    PET = 'Pet', 'pet'
