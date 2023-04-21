"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth import views as auth_views

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View

class RegistreraAnvändare(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registrera.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'registrera.html', {'form': form})


urlpatterns = [
    path('', include('cart.urls')),
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
    path('registrera/', RegistreraAnvändare.as_view(), name='registrera-användare'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
