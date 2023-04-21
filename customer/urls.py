from django.urls import path
from .views import CustomerRegistrationView

app_name = 'customer'

urlpatterns = [
    path('register/', CustomerRegistrationView.as_view(), name='register'),
]