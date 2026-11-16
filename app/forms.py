from django import forms
from .models import *



class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Productform(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'