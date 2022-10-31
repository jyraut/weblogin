
from django import forms
from django.contrib.auth.models import User


class reg_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']


# Create your models here.
