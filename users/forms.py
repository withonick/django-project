from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ImageField, FileInput, HiddenInput

from .models import Profile


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input-line full-width'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['class'] = 'input-line full-width'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['class'] = 'input-line full-width'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'input-line full-width'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        #     'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        # }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

