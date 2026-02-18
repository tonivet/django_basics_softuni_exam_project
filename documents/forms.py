from django import forms

from .models import DocumentsModel
from .choices import DocumentTypeChoices

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = DocumentsModel
        fields = ['title', 'type', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Заглавие'}), 
            'type': forms.Select(attrs={'class':'form-control'}), 
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

