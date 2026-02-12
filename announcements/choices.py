from django.db import models

class StatusChoices(models.TextChoices):
    ACCEPTED = 'Accepted', 'Приета'
    IN_PROGRESS = 'In Progress', 'Изпълнява се'
    DONE = 'Done', 'Изпълнена'

