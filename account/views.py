from django.shortcuts import render
from . models import *


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    context = {'orders': orders, 'customers': customers}
    
    return render(request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})