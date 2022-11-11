from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	phone_no = forms.CharField(max_length = 20)
	first_name = forms.CharField(max_length = 20)
	last_name = forms.CharField(max_length = 20)
	class Meta:
		model = User
		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class ValueForm(forms.Form):
    class Meta:
        model = Value
        fields = ['input_value', 'search_value']

# class khojForm(forms.Form):
#     # name = forms.CharField()
#     input_value = forms.CharField(max_length = 100)
#     search_value = forms.IntegerField(help_text="Enter a number to search")
