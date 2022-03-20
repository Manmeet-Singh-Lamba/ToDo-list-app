from django import forms 

from .models import List, Task

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
