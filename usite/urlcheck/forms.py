from django import forms
from .models import URL
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class URLAddForm(forms.ModelForm):
    class Meta():
        model = URL
        fields = ('site_name', 'site_url', 'interval')


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'password')
