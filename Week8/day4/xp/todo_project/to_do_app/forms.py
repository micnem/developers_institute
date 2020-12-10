from django import forms
from django.forms import ModelForm
from .models import Todo, Category

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'deadline_date', 'category']

class MarkCompleteForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['has_been_done']
    