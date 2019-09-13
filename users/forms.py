from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hood.models import NeighbourHood

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    id=forms.IntegerField()


    class Meta:
        model=User
        fields=['username','email','id','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']
                