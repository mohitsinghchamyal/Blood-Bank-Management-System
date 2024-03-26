from django import forms
from django.contrib.auth.models import User
from . import models

class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password']
        widgets={'password': forms.PasswordInput()}

class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['bloodgroup','address','mobile','profile_pic']