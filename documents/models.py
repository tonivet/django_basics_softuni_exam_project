from django.db import models
from django.core.validators import FileExtensionValidator

from .validators import MaxFileSizeValidator
from .choices import DocumentTypeChoices

# Create your models here.

class DocumentsModel(models.Model):
    title = models.CharField(max_length=55)
    type = models.CharField(max_length=25, choices=DocumentTypeChoices, default=DocumentTypeChoices.INVOICE)
    file = models.FileField(upload_to='documents/', validators=[
        FileExtensionValidator(allowed_extensions=['doc', 'pdf', 'jpg', 'jpeg', 'png']),
        MaxFileSizeValidator(max_size_mb=5)
    ])
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

