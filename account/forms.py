from django import forms
from django.db import models
from django.db.models import fields
from .models import User,Address
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=200)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email')

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=('state','city','address','post_code','plaque','unit','phone_number')

