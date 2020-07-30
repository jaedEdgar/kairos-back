from django.urls import path, include
from . import views

urlpatterns = [
    path('api/notebooks', views.NotebookListCreate.as_view()),
    path('api/notebook/<int:pk>', views.NotebookUpdate.as_view()),
    path('api/tasks', views.TaskListCreate.as_view()),
    path('api/task/<int:pk>', views.TaskUpdate.as_view()),
]
