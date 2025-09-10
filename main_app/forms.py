from django import forms
from .models import Result, Helmet
class HelmetForm(forms.ModelForm):
    class Meta:
        model = Helmet
        fields = ['name', 'color', 'image']

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['date', 'session', 'position']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date', 'placeholder': 'Select a date'}
            ),
        }