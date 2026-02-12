from django.db.models import TextChoices

class CitizenRole(TextChoices):
    CONDOMINIUM_MANAGER = 'Condominium manager', 'condominium manager'
    CONDOMINIUM_CASHIER = 'Condominium cashier', 'condominium cashier'
    RESIDENT = 'Resident', 'Resident'

class FlatRole(TextChoices):
    OWNER = 'Owner', 'Собственик'
    RESIDENT = 'Resident', 'Обитател'
    TENANT = 'Tenant', 'Наемател'
    PET = 'Pet', 'Домашен любимец'
