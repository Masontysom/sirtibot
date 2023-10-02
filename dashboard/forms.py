from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"

# from django import forms
# from .models import GeneratedMCQ  # Import your model

# class GeneratedMCQForm(forms.ModelForm):
#     class Meta:
#         model = GeneratedMCQ
#         fields = ['question', 'options', 'correct_option','mcq_text']  # Add the appropriate fields from your model
