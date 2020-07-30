from django.contrib import admin
from .models import Notebook, Task
# Register your models here.


class NotebookAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Task, TaskAdmin)
