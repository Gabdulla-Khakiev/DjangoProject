from django.urls import path
from .views import ProductListView, ProductDetailView, ContactsView, AddProductView
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add/', AddProductView.as_view(), name='add_product'),
]
