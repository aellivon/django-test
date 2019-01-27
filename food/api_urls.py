from .api import ProductViewSet
from django.urls import path

create_product = ProductViewSet.as_view({
    'get': 'list_of_food',
    'post': 'create_product',
})

product = ProductViewSet.as_view({
    'get': 'list_of_products',
})


app_name = 'food'

urlpatterns = [
    path('product/create/', create_product, name='create_product'),
    path('product/', product, name='product')
]