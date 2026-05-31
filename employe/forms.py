from django import forms
from .models import Employe

class EmployeForms(forms.ModelForm):
    class Meta:
        model : Employe
        fiels= ["nom","email","poste","salaire"]