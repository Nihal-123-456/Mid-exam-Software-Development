from django import forms
from django.contrib.auth.models import *
from django.contrib.auth.forms import *

class register(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'required'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class edit_profile(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']