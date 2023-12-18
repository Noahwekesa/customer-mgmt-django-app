from django.contrib.admin.options import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from accounts.models import *
from .forms import OrderForm

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


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'accounts/order_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Order has been created succefully!')
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'accounts/order_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Order has been updated succefully!')
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'accounts/delete.html'
    success_url = "/"

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.author:
            return True
        return False
