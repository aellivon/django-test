from django.db import models


class Food(models.Model):
    """
        Class for food
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    """
        Class for product
    """
    name = models.CharField(max_length=255)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food')

    def __str__(self):
        return f"{self.name}"
