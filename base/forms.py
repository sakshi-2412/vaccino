from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['roll_no', 'branch', 'program', 'year', 'age', 'gender']

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class VaccForm(ModelForm):
	class Meta:
		model = VaccDetails
		fields = ['reference_id', 'vaccine_name', 'dose_taken', 'date1', 'date2', 'certificate']
		widgets = {
            'date1': DateInput(),
            'date2': DateInput()
        }

class HistoryForm(ModelForm):
	class Meta:
		model = CovidHistory
		fields = ['infected','date']
		widgets = {
            'date': DateInput()
        }