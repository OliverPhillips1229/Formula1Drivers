from django import forms
from .models import Driver, Result, Helmet

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'current_team', 'description', 'age', 'drive_years', 'helmets']
        widgets = {
            'helmets': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show all helmets, but keep already owned helmets selected
        if self.instance.pk:
            self.fields['helmets'].queryset = Helmet.objects.all()

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