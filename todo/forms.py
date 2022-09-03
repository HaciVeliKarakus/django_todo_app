from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from todo.models import Todo


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
