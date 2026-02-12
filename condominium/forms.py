from django import forms

from .models import FlatResident
from .mixin import DisableFormFieldsMixin
from .choices import FlatRole

class FlatResidentForm(forms.ModelForm):
    class Meta:
        model = FlatResident
        fields = ['first_name', 'last_name', 'phone', 'email', 'flat', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Име'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Телефон'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email'}),
            'flat': forms.Select(attrs={'class':'form-control'}),
            'role': forms.Select(attrs={'class':'form-control'}),
        }

class FlatResidentDeleteForm(DisableFormFieldsMixin, FlatResidentForm):
    ...


class ResidentRoleFilterForm(forms.Form):
    # adding empty string to the list of choices with all value to be able to clear previous filters and show all 
    role = forms.ChoiceField(
        choices=[('', "Всички")] + list(FlatRole.choices),  
        required=False
    )


class ResidentSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        label='',
        required=False,
    )

