from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Food, Product
from .serializers import FoodSerializer, CreateProductSerializer, ListProductSerializer

class ProductViewSet(ViewSet):
    """
        Product viewset
    """

    def list_of_food(self, *args, **kwargs):
        """
            gets the list of randomzier
        """
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=200)

    def create_product(self, *args, **kwargs):

        # Shoving the data to our serializer that was send by the request
        serializer = CreateProductSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def list_of_products(self, *args, **kwargs):

        products = Product.objects.all()
        serializer = ListProductSerializer(products, many=True)
        return Response(serializer.data, status=200)