from django import forms
from django.forms import ModelForm
from .models import Registration

from django.contrib.auth import authenticate , login , logout , get_user_model

class LoginForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['Name', 'Password' ]
