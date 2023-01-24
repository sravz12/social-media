from django import forms
from socialapp.models import Myuser
from django.contrib.auth.forms import UserCreationForm
from socialapp.models import Photos





class RegistrationForm(UserCreationForm):
    
    class Meta():
        model=Myuser
        fields=["first_name",
        "last_name",
        "username",
        "email",
        "phone",
        "profile_pic",
        "password1",
        "password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photos
        fields={
            "image",
            "description"
        }
        widgets={
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-select"})
        }