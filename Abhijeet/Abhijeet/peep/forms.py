# forms.py
from django import forms
from .models import Peep

class PeepForm(forms.ModelForm):
    class Meta:
        model = Peep
        fields = ['text', 'photo']
