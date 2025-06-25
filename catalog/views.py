from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from catalog.models import Product
from catalog.forms import ProductForm
from django.core.paginator import Paginator


def home(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 6)  # 6 товаров на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})


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
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})
