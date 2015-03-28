#encoding:utf-8
from django import forms
from security.models import Usuario

class LoginForm(forms.Form):
	username = forms.CharField(label = "Usuario", max_length = 250)
	password = forms.CharField(label = "Contaseña", widget = forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['is_staff', 'last_login', 'date_joined', 'is_superuser', 'user_permissions','groups']
