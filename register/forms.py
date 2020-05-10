from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


# forms for email and other things are added and ordered
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ReserPassword(PasswordResetForm):
    resetpasswors = forms.PasswordInput()

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
