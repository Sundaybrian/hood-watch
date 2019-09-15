from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hood.models import NeighbourHood,Location,Business
from users.models import Profile





class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    IDNumber=forms.IntegerField()


    class Meta:
        model=User
        fields=['username','email','IDNumber','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','bio']     


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['location','hood','owner']




class AddNeighbourhoodForm(forms.ModelForm):
  
    class Meta:
        model=NeighbourHood
        fields=['hoodname']


class AddLocationForm(forms.ModelForm):
  
    class Meta:
        model=Location
        fields=['locationName']        

