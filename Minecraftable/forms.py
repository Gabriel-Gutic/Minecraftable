from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Datapack


class LoginForm(forms.Form):
    username_email = forms.CharField(label='Username or Email', max_length=100, widget=forms.TextInput(attrs={'id': 'username-email-field', 'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'id': 'password-field', 'class': 'form-control'}))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id': 'remember-me'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'id': 'username-field', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'id': 'email-field', 'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'id': 'password-field', 'class': 'form-control'}))
    password_again = forms.CharField(label='Password(again)', max_length=50, widget=forms.PasswordInput(attrs={'id': 'password-again-field', 'class': 'form-control'}))


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'id': 'password-field', 'class': 'form-control'}), required=False)
    password_again = forms.CharField(label='Password(again)', max_length=50, widget=forms.PasswordInput(attrs={'id': 'password-again-field', 'class': 'form-control'}), required=False)


class NewDatapackForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={'id': 'name-field'}))
    description = forms.CharField(label='Description', required=False, max_length=200, widget=forms.TextInput(attrs={'id': 'description-field'}))
    version = forms.ChoiceField(label='Version', choices=Datapack.VERSIONS, widget=forms.Select(attrs={'id': 'version-field'}))