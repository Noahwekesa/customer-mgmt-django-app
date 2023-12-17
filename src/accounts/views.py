from django.shortcuts import render

from accounts.models import Product


def dashboard(request):
    context = {}
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/products.html", context)

def customer(request):
    context = {}
    return render(request, "accounts/customer", context)
