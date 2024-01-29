# Example: Adding a new field to an existing model
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    new_field = models.CharField(max_length=50)  # New field


class Meta:
    app_label = "employee"
