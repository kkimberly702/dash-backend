from rest_framework import serializers
from ..models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'photo', 'category', 'brand', 'review', 'author', 'created_or_updated_at')