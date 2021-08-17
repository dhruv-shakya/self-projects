# forms.py 
from django import forms 
from .models import *


class Post_form(forms.ModelForm): 

	class Meta: 
		model = Post 
		fields = ['pic']
