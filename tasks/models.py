from django.db import models

# Create your models here.


class Notebook(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'created_at'

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.IntegerChoices):
        IS_NOT_CHECKED = 1
        IS_CHECK = 2
        IS_DELETE = 3
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        order_with_respect_to = 'created_at'

    def __str__(self):
        return self.name
