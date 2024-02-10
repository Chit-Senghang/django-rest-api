# models.py
from django.db import models

from src.category.models import Category


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table = 'item'
