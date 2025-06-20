from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Product
from catalog.forms import ProductForm


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def contacts(request):
    if request.method == "POST":
        return HttpResponse("Мы с вами свяжемся.")
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # или на страницу товара
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
