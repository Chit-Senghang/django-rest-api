from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'category'
