from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product


# Create your views here.
def home_view(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Вывод последних продуктов в консоль
    for product in latest_products:
        print(f"Product ID: {product.id}, Name: {product.name}, Created At: {product.created_at}")

    # Передача данных в шаблон
    return render(request, 'catalog/home.html', {'latest_products': latest_products})


def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


    return render(request, 'catalog/contacts.html')
