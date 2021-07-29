from django.core import validators
from django import forms
from django.forms import fields
from .models import Soils

class SoildForm(forms.Form):
      Sample= forms.CharField(max_length=100)
      Sand= forms.CharField(max_length=100)
      Silt= forms.CharField(max_length=100)
      Clay= forms.CharField(max_length=100)
      Type= forms.CharField(max_length=100)
      Image = forms.FileField()