from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('avatar','username', 'country','email', 'phone_number','password1', 'password2')


