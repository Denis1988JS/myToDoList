from django.contrib import admin
from django.urls import path
from todos.views import index, register, login_user, logout_user, addTask, changeStatusTask, deleteTask

urlpatterns = [
    path('',index, name='home'),#Главная страница приложения - todos
    path('register/',register, name='register'),#Регистрация пользователя
    path('login/',login_user, name='login'),#Регистрация пользователя
    path('logout/',logout_user,name='logout'),#выход из авторизации
    path('addTask/',addTask,name='addTask'),#добавление задачи
    path('changeStatusTask/<int:id>',changeStatusTask,name='changeStatusTask'),#пометить выполненным
    path('deleteTask/<int:id>',deleteTask,name='deleteTask'),#пометить выполненным
]