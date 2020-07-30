from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Notebook, Task
from .serializers import NotebookSerializer, TaskSerializer
# Create your views here.


class NotebookListCreate(generics.ListCreateAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class NotebookUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class TaskListCreate(generics.ListCreateAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        notebook = self.request.query_params.get('notebook')

        if notebook:
            queryset = queryset.filter(notebook=notebook)

        return queryset


class TaskUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
