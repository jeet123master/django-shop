from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None