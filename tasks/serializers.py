from rest_framework import serializers
from .models import Notebook, Task


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('notebook', 'id', 'name', 'description', 'status')
