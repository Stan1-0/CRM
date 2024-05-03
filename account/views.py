from django.shortcuts import render
from . models import *


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers, 'total_orders':total_orders, 'delivered': delivered, 'pending': pending, 'total_customers': total_customers}
    
    return render(request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})