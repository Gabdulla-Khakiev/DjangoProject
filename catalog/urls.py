from django.urls import path
from .views import home, contacts, product_detail, add_product
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
]
