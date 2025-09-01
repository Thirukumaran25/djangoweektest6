from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    add_to_cart,
    remove_from_cart,
    view_cart,
    register,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='cart'),
    path('accounts/register/', register, name='register'),
]