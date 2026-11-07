from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    telefono = forms.CharField(label="Teléfono", max_length=15)
    direccion = forms.CharField(label="Dirección", max_length=250)

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)