from django.shortcuts import render
from . models import Customer
from . models import Products

# Create your views here.
def home(request):
    return render(request, 'dashboard.html')

def products(request):
    produtcs = Products.objects.all()
    return render(request, 'products.html')

def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers': customers})