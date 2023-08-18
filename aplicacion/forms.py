from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class WineForm(forms.Form):
    categoria = forms.CharField(label="Categoria del Vino", max_length=50, required=True)
    uva = forms.CharField(label="Uva", max_length=50, required=True)

class SpiritForm(forms.Form):
    categoria = forms.CharField(label="Categoria del Spirit", max_length=50, required=True)
    producto = forms.CharField(label="Producto", max_length=50, required=True)
    marca = forms.CharField(label="Marca", max_length=50, required=True)

class BeerForm(forms.Form):
    estilo = forms.CharField(label="Stile of beer", max_length=50, required=True)
    color = forms.CharField(label="Color", max_length=50, required=True)


class RegisterUsersForm(UserCreationForm):
    email = forms.EmailField(label="Email User")
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email User")
    password1= forms.CharField(label="Password", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        help_text = { k:"" for k in fields}

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)