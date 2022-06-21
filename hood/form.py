from .models import Bussiness, Neighbourhood, Post, Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ('admin',)



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','timestamp']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    bio = forms.CharField() 

    class Meta:
        model = User
        fields = ['username','email']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Bussiness
        exclude = ('user', 'neighbourhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'neighbourhood')
        