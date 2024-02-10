# serializers.py
from rest_framework import serializers

from src.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Category
        fields = '__all__'
