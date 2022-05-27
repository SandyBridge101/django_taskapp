from asyncio import tasks
from dataclasses import field
from pyexpat import model
from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):#for save
    class Meta:
        model=TaskModel
        fields=['task',]

class TaskUpdateForm(forms.ModelForm):#for edit
    class Meta:
        model=TaskModel
        fields='__all__'