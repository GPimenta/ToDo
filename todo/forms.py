from django import forms

from todo.models import ToDo


class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"
