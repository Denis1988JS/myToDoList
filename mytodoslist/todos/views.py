from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.checks import messages
from django.db.models import Count, QuerySet
from django.shortcuts import render, HttpResponse, redirect
from todos.forms import UserRegisterForm, UserLoginForm, AddTask
from todos.models import Task
from  django.contrib import messages

# Create your views here.
#Главная страница
def index(request):
    title = 'Веб приложение - мой список дел'
    if request.user.is_authenticated == True:
        form = AddTask()
        userName = request.user
        userTask = Task.objects.filter(user=userName).values().annotate().order_by()
        data = {"title":title, "userTask":userTask,"form":form}
        return render(request, 'index.html', context=data)
    else:
        message="Добро пожаловать на Веб приложение - мой список дел "
        data = {"title": title,"message":message }
        return render(request, 'index.html', context=data)
#Регистрация пользователей
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'Регистрация успешна')
            return redirect('home')
        else:
            messages.error(request, 'Не авторизован')
            print(messages)
    else:
        form = UserRegisterForm()
        title = 'Регистрация'
    data = {'form':form,'title':title}
    return render(request, 'register.html', context=data)
#Авторизация пользователя
def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Авторизация не успешна')
            return redirect('login')
    else:
        form = UserLoginForm()
        title = 'Авторизация'
        data = {'form':form,'title':title}
        return render(request, 'login.html', context=data)
#Выход пользователя
def logout_user(request):
    logout(request)
    return redirect('home')

#Страница - добваление задачи - причем через action
def addTask(request):
    userId = request.user.id
    form = AddTask(request.POST, request.FILES)
    if form.is_valid():
        form.cleaned_data['user_id'] = userId
        Task.objects.create(**form.cleaned_data)
        return redirect('home')
    else:
        messages.error(request, 'Ошибка в добавлении задачи')
        return redirect('home')

#Пометить как прочитанное
def changeStatusTask(request, id):
    task = Task.objects.get(id=id)
    task.statusChange()
    task.save()
    return redirect('home')

#Удалить задачу
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')
