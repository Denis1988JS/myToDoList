import re
from django import forms
from django.core.exceptions import ValidationError #Валидация формы
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from  django.contrib.auth.models import User
from django.http import request

from todos.models import Task


#Форма регистрации пользователей

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='Ваш логин', widget=forms.TextInput({'class': 'form-control'}))
    email = forms.EmailField(max_length=70, label='Ваш емаил', widget=forms.EmailInput({'class': 'form-control'}))
    telNumber = forms.CharField(max_length=25, label='Ваш номер телефона', widget=forms.TextInput({'class': 'form-control'}))
    first_name = forms.CharField(max_length=20, label='Ваше имя', widget=forms.TextInput({'class': 'form-control', 'title': 'Ваше имя'}))
    last_name = forms.CharField(max_length=20, label='Ваша фамилия', widget=forms.TextInput({'class': 'form-control'}))
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput({'class': 'form-control', "autocomplete": 'off'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput({'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2','email','telNumber']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'telNumber': forms.TextInput()
        }

#Форма авторизации пользователя

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='Ваш логин', widget=forms.TextInput({'class': 'form-control'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput({'class': 'form-control', "autocomplete": 'off'}))


#Форма добавления задачи - на основе класса
class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','content','dateOfCompletion','imageTask']
        labels = {
            'title': 'Задача',
            'content': 'Содержание задачи',
            'dateOfCompletion': 'Дата выполнения',
            'imageTask': 'Картинка',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'dateOfCompletion':forms.DateInput(attrs={'type': 'date'}),
        }