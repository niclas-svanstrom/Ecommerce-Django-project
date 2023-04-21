from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, update_cart

urlpatterns = [
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart/<int:product_id>/', update_cart, name='update_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart, name='cart'),
]