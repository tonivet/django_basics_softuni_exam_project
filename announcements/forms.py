from django import forms

from .models import Announcements
from .choices import StatusChoices


class AnnouncementsFrom(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'text', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Заглавие'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }

class StatusFilterForm(forms.Form):
        status = forms.ChoiceField(
             choices = [('', 'Всички')] + list(StatusChoices.choices),
             required = False
        )
