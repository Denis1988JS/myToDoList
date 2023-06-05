from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from django.core import validators
# Create your models here.

#Модель - task / задача

class Task(models.Model):
    title = models.CharField(max_length=50, validators=[validators.RegexValidator(regex='^[^<>/]')] ,verbose_name='оглавление')
    content = models.TextField(max_length=500, verbose_name='описание')
    status = models.BooleanField(default=False)
    dateCreate = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    dateOfCompletion = models.DateField(verbose_name='Срок выполнения')
    imageTask = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name = 'Фото')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    def __str__(self):
        return (f'{self.title} от {self.dateCreate}')
    def statusChange(self):
        self.status = True
        return print(self.status, 'Метод')

    class Meta:
         verbose_name = 'Задача'
         verbose_name_plural = 'Задачи'
         ordering = ['id']
    def get_absolute_url(self):
        return reverse_lazy('task', kwargs={'id': self.pk})#task/id
