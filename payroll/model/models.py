# Example: Adding a new field to an existing model
from django.db import models


class Payroll(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
