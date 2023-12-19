from django.contrib.admin.options import inlineformset_factory, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from accounts.filters import OrderFilter
from accounts.models import *
from .forms import CreateUserForm, OrderForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Regstration Was Succefully")
                return redirect('login')
        context = {
        "form":form
        }
        return render(request, 'accounts/register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have Ended Your session")
    return redirect('login')

@login_required
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

@login_required
def products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "accounts/products.html", context)

class CustomerView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "accounts/customer.html"
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        orders = customer.order_set.all()
        order_count = orders.count()
        
        myFilter = OrderFilter(self.request.GET, queryset=orders)
        orders = myFilter.qs

        context['orders'] = orders
        context['order_count'] = order_count
        context['myFilter'] = myFilter
        return context
''''
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'accounts/order_form.html'
    success_url = reverse_lazy('dashboard')

    '''
@login_required
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)

# update order class based view
class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'accounts/order_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Order has been updated succefully!')
        return super().form_valid(form)

class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.author:
            return True
        return False
