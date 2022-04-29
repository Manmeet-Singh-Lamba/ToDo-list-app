from logging import PlaceHolder
from django import forms
from matplotlib import widgets 

from .models import List, Task

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ("list_name", "status")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("task_name", "task_description", "Completed")
