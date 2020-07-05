from django.shortcuts import render
from rest_framework import generics
from .models import Notebook, Task
from .serializers import NotebookSerializer, TaskSerializer
# Create your views here.


class NotebookListCreate(generics.ListCreateAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
