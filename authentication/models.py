# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        # Specify the custom table name
        db_table = 'user'
