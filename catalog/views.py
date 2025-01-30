from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm
from catalog.models import Product

class HomeTemplateView(TemplateView):

    template_name = 'catalog/home.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/createProduct.html'
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/updateProduct.html'
    success_url =  reverse_lazy('products')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")

        return product

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    from_class = ProductForm
    template_name = 'catalog/productDelete.html'
    success_url =  reverse_lazy('products')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")
        return product

class  ProductListView(ListView):
    model =  Product

    



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'



class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

class UnpublishProductView(LoginRequiredMixin, View):
    success_url = reverse_lazy('products')
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        # Проверка прав пользователя
        if not request.user.has_perm('user.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        # Логика отмены публикации
        if product.is_public == False:
            product.is_public = True
            product.save()

        return redirect('products')


class DeleteProductView(LoginRequiredMixin, View):
    def post(self,  request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления")

        product.delete()
        return redirect('products')




