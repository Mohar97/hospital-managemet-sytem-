from django import forms
from .models import Patient
from .models import Ambulance

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact', 'address', 'department', 'doctor']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'age': forms.NumberInput(attrs={'class': 'form-input'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea'}),
            'department': forms.TextInput(attrs={'class': 'form-input'}),
            'doctor': forms.TextInput(attrs={'class': 'form-input'}),
        }



class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['vehicle_number', 'driver_name', 'contact', 'is_available']
