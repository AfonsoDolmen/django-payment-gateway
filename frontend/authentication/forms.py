from django import forms
from email_validator import validate_email, EmailNotValidError
import re


class LoginForm(forms.Form):
    # Campos do formulário
    email = forms.EmailField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail',
        }))

    password = forms.CharField(
        max_length=250, widget=forms.PasswordInput(attrs={
            'class': 'form-control w-100',
            'placeholder': 'Digite sua senha'
        }))

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get('email', '')

        try:
            email = validate_email(email, check_deliverability=False).email
        except EmailNotValidError:
            raise forms.ValidationError('Digite um e-mail válido.')

        return cleaned_data


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite seu melhor e-mail',
    }))

    password = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite uma senha',
    }))

    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Digite sua senha novamente',
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email', '')

        if email is None:
            raise forms.ValidationError('Campo de e-mail é obrigatório.')

        # Valida o email
        try:
            email = validate_email(email, check_deliverability=False).email
        except EmailNotValidError:
            raise forms.ValidationError('Digite um e-mail válido.')

        return email

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password', '')
        password2 = cleaned_data.get('password2', '')
        pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{3,}$'

        if not password or not password2:
            raise forms.ValidationError('Campo de senha não pode ser vazio.')

        if not re.match(pattern, password):
            raise forms.ValidationError(
                'A senha deve conter: no mínimo 3 caracteres, uma letra maiúscula e um caractere especial.')

        if password != password2:
            raise forms.ValidationError('As senhas devem ser iguais.')

        return cleaned_data
