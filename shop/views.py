from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Product

def index(request):
    text1 = "Welcome to the shop butta"
    return HttpResponse(text1)

#Category View

def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products = Product.objects.filter(Category=c_page,available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'shop/category.html',{'category':c_page,'products':products})