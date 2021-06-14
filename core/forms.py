

from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
import re
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class Loginlikendin(UserCreationForm):
    email=forms.CharField(max_length=200,min_length=1,required=True, validators=[
        RegexValidator(
            regex='^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$',
            message='Introduce un email válido',
            code='invalid_email'
        ),
    ])
 
    class Meta:
        model = User
        fields = ('username',
'email', 'password1', 'password2',)




 
class Scrappingform(forms.Form):
    localization=forms.CharField(max_length=50, required=True)
    name=forms.CharField(max_length=200,required=True)
    pages=forms.IntegerField(required=True)
    

class Passwordform(forms.Form):
    LikendinContraseña=forms.CharField(max_length=500,required=True,label='Likendin Contraseña')

class VisitedForm(forms.Form):
    LikendinContraseña=forms.CharField(max_length=500,required=True,label='Likendin Contraseña')
