from django.db import models

# Create your models here.
class Announcements(models.Model):
    class StatusChoices(models.TextChoices):
        ACCEPTED = 'Accepted', 'Accepted'
        IN_PROGRESS = 'In Progress', 'In Progress'
        DONE = 'Done', 'Done'

    title = models.CharField(max_length=125)
    text = models.TextField()
    author = models.ForeignKey('condominium.FlatResident', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=StatusChoices, default=StatusChoices.ACCEPTED)

    def __str__(self):
        return self.title

