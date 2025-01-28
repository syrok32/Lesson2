from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from catalog.models import Product

class HomeTemplateView(TemplateView):

    template_name = 'catalog/home.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/createProduct.html'
    success_url = reverse_lazy('products')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/updateProduct.html'
    success_url =  reverse_lazy('products')

class ProductDeleteView(DeleteView):
    model = Product
    from_class = ProductForm
    template_name = 'catalog/productDelete.html'
    success_url =  reverse_lazy('products')

class  ProductListView(ListView):
    model =  Product



class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


