from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_("Password"), min_length=8, widget=forms.PasswordInput, show_hidden_initial=True)
    password2 = forms.CharField(label=_("Repeap Password"), min_length=8, widget=forms.PasswordInput, show_hidden_initial=True)

    class Meta:
        model  = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
