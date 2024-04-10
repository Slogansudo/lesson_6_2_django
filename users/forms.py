
from django.contrib.auth.models import User
from django import forms
from .models import Level


class StudentsLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class StudentsRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)
    status = forms.ChoiceField(choices=Level.choices)
    password_1 = forms.CharField(max_length=200)
    password_2 = forms.CharField(max_length=200)
