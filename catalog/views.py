from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, 'catalog/home.html')


def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


    return render(request, 'catalog/contacts.html')
