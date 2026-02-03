from django.db.models import TextChoices

class BillsFeeChoices(TextChoices):
    ELECTRICITY = 'Electricity', 'electricity'
    WATER = 'Water', 'water'
    ELEVATOR_TAX = 'Elevator tax', 'Elevator tax'
    CLEANER = 'Cleaner', 'cleaner'
    DOORMAN = 'Doorman', 'doorman'
    GARDENER = 'Gardener', 'gardener'
    OTHER = 'Other', 'other'
