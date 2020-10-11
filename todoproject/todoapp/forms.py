from django import forms
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['task','description','task_time','is_important']
        widgets = {
            'task': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'task_time': forms.TextInput(attrs={'class': 'form-control'}),
            'is_important': forms.CheckboxInput(),
        }
