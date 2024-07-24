from django import forms
from django.contrib.auth.models import User
from .models import EmailCodeModel


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': 'Please enter your username!',
        'max_length': 'Username length: 2 to 20.',
        'min_length': 'Username length: 2 to 20.'
    })
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email address!',
        'invalid': 'Please enter a valid email!'
    })
    email_code = forms.CharField(max_length=4, min_length=4, error_messages={
        'required': 'Please enter your verification code!',
        'max_length': 'Code length: 4.',
        'min_length': 'Code length: 4.'
    })
    password = forms.CharField(max_length=20, min_length=1, error_messages={
        'required': 'Please enter your password!',
        'max_length': 'Password length: 1 to 20.',
        'min_length': 'Password length: 1 to 20.'
    })

    # "clean" means transforming user inputs to standard data format
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists!')
        return email

    # Verify email_code and email address combo
    def clean_email_code(self):
        email = self.cleaned_data.get('email')
        email_code = self.cleaned_data.get('email_code')

        if not EmailCodeModel.objects.filter(email=email, email_code=email_code).first():
            raise forms.ValidationError('Invalid email or code!')
        return email_code


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email address!',
        'invalid': 'Please enter a valid email!'
    })
    password = forms.CharField(max_length=20, min_length=1, error_messages={
        'required': 'Please enter your password!',
        'max_length': 'Password length: 1 to 20.',
        'min_length': 'Password length: 1 to 20.'
    })
    remember = forms.BooleanField(required=False)
