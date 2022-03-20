from subprocess import CompletedProcess
from tkinter import CASCADE
from django.db import models
import string

def generate_unique_code():
    length = 6

    #while True:


# Create your models here.
class List(models.Model):
    list_name           = models.CharField(max_length = 50, default="", unique=True)
    status              = models.BooleanField(null=False, default =  False)
    created_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.list_name

class Task(models.Model):
    todolist            = models.ForeignKey(List, on_delete=models.CASCADE)
    task_name           = models.CharField(max_length = 50, default="", unique=True)
    task_description    = models.TextField(max_length= 160, default = "describe the task here")
    Completed           = models.BooleanField(null=False, default =  False)

    def __str__(self) -> str:
        return self.task_name