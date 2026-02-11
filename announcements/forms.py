from django import forms

from .models import Announcements
# from condominium.mixin import DisableFormFieldsMixin


class AnnouncementsFrom(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['title', 'text', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Заглавие'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }

class StatusFilterForm(forms.ModelForm):
    class Meta:
        model = Announcements
        fields = ['status']
