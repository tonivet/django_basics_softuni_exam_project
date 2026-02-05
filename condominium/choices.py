from django.db.models import TextChoices

class CitizenRole(TextChoices):
    CONDOMINIUM_MANAGER = 'Condominium manager', 'condominium manager'
    CONDOMINIUM_CASHIER = 'Condominium cashier', 'condominium cashier'
    RESIDENT = 'Resident', 'Resident'

class FlatRole(TextChoices):
    OWNER = 'Owner', 'собственик'
    RESIDENT = 'Resident', 'живущ'
    TENANT = 'Tenant', 'наемател'
    PET = 'Pet', 'домашен любимец'
