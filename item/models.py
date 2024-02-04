# models.py
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()

    class Meta:
        db_table = 'item'

    def __str__(self):
        return self.name
