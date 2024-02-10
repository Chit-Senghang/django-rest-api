# serializers.py
from rest_framework import serializers

from src.item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.FloatField()
    category_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
