from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""
Login form with authentication of credentials.
"""


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(**cleaned_data)
        if user is None:
            raise ValidationError("Niepoprawne dane.")
        cleaned_data['user'] = user
        return cleaned_data


"""
Registration form with validation of passwords. Checks if username is already used.
"""


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError("Hasła się nie zgadzają.")
        return cleaned_data

    class Meta:
        model = User
        fields = ['username']