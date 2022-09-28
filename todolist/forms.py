from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        error_messages = {
                'required' : 'This field is required'
        }
        title = forms.CharField(
                    label='Task Title', 
                    required=True,
                    max_length=255, 
                    widget=forms.TextInput(attrs={
                        'type': 'text',
                        'placeholder': 'Enter task title',
                    })
                )
        description = forms.CharField(
                    label='Task Description',
                    required=True,
                    widget=forms.Textarea(attrs={
                        'type': 'text',
                        'placeholder': 'Enter the task description',
                    }) 
                )   