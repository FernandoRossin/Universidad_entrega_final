from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Curso_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Estudiante_formulario(forms.Form):

   nombre = forms.CharField(max_length=40)
   apellido = forms.CharField(max_length=40)
   email = forms.EmailField()

class Profesor_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=40)


class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repatir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['email','password1', 'password2']
        help_text =  {k: "" for k in fields}

class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    email = forms.EmailField(label='email')  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput)  
