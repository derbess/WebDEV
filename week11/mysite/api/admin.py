from django.contrib import admin
from .models import Task
from .models import TaskList

# Register your models here.

admin.site.register(TaskList)
admin.site.register(Task)

