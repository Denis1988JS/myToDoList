from django.contrib import admin
from django.utils.safestring import mark_safe

from todos.models import Task
# Register your models here.

#Модель редактора для задачи
class TaskInline(admin.StackedInline):
    model = Task

#Модель отображения задачи
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','status','dateCreate','dateOfCompletion','get_html_photo','imageTask','user']
    list_display_links = ['id','title','user']
    list_editable = ('status',)
    list_select_related = True
    ordering = ['user','id']
    search_fields = ['title','user']
    list_filter = ('dateCreate','dateOfCompletion','user__username',)
    def get_html_photo(self, object):
        if object.imageTask:
            return mark_safe(f"<img src='{object.imageTask.url}' width=35>")
    get_html_photo.short_description = 'Фото'

admin.site.register(Task,TaskAdmin)




admin.site.site_title = 'Панель администратора сайта'
admin.site.site_header = 'Панель администратора сайта'
