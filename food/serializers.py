from rest_framework import serializers

from .models import Food, Product

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('id', 'name')

class ListProductSerializer(serializers.ModelSerializer):
    """
        This serializer, gets the food and is expecting a dictionary
    """
    food = FoodSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'food')

class CreateProductSerializer(serializers.ModelSerializer):
    """
        This serializer expects  id
    """
    class Meta:
        model = Product
        fields = ('name', 'food')

