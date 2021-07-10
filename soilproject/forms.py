from django.core import validators
from django import forms
from django.forms import fields
from .models import Students

class StudentForm(forms.Form):
      Name= forms.CharField(max_length=100)
      Image = forms.FileField()