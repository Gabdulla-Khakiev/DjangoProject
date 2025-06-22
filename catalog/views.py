from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from catalog.models import Product
from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product
    paginate_by = 6
    ordering = ['-created_at']


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def render_to_response(self, request, *args, **kwargs):
        return HttpResponse("Мы с вами свяжемся.")


class ProductDetailView(DetailView):
    model = Product


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")
