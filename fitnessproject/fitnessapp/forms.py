from django import forms
from .models import fitnessmodel



class fitnessform(forms.ModelForm):
    class Meta:
        model = fitnessmodel
        fields = '__all__'

