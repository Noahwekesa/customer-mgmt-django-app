"""
URL configuration for crm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('products/', products, name='products'),
    path('customer/<int:pk>/', CustomerView.as_view(), name='customer-detail'),
    path('order/create', OrderCreateView.as_view(), name='order-create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
]
