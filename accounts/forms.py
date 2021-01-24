from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms

class UserCreateForm(UserCreationForm):
    
    class Meta:
        model  = User 
        fields = ('first_name','last_name','username','email','password1','password2')
        
        widgets = {
            'username':forms.TextInput(attrs={ 'placeholder':'User Name'}),
            'email':forms.EmailInput(attrs={ 'placeholder':'Email Adress'}),
           
        } 

class LoginForm(AuthenticationForm):
    class Meta:

        widgets = {
            'username':forms.TextInput(attrs={ 'class':"form-control",'placeholder':'User Name'}),
            'password':forms.EmailInput(attrs={ 'class':"form-control",'placeholder':'*********'}),
           
        }