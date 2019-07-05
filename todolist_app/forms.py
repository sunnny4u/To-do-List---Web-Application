from django import forms
from .models import Taskmate

class Taskform(forms.ModelForm):
	class Meta:
		model = Taskmate
		fields = ['task', 'done']
