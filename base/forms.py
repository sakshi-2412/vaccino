from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['roll_no', 'branch', 'program', 'year', 'age', 'gender']

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password']