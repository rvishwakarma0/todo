from django import forms
from .models import Task

class ImageForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ["image"]
