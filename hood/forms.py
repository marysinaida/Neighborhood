from django import forms
from .models import Neighborhood

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude =['name','location']