from django import forms
from django.db.models import fields
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['address']
        widgets = {'address': forms.HiddenInput()}        