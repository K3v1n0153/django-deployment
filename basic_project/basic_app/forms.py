from django import forms
from django.contrib.auth.models import User
from django.core import validators
from basic_app.models import UserProfileInfo

def password_length(value):

	if len(value) < 8:
		raise forms.ValidationError("Password should have 8 characters long.")

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput(), validators=[password_length])
	botcatcher = forms.CharField(required=False, 
								 widget=forms.HiddenInput(), 
								 validators=[validators.MaxLengthValidator(0)])

	class Meta:

		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

	class Meta:

		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_picture')