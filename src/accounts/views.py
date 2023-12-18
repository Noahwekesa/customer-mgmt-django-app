from django.shortcuts import render
from django.views.generic import DetailView
from accounts.models import *


def dashboard(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        "customers": customers, 
        "orders": orders,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "delivered": delivered,
        "pending": pending,

    }
    return render(request, "accounts/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/products.html", context)

class CustomerView(DetailView):
    model = Customer
    template_name = "accounts/customer.html"
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        orders = customer.order_set.all()
        order_count = orders.count()
        context['orders'] = orders
        context['order_count'] = order_count
        return context
