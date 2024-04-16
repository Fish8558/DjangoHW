from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    context = {
        "object_list": Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    contact = Contact.objects.get(pk=1)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name} / Телефон: {phone} / Сообщение: {message}")
    return render(request, 'catalog/contacts.html', context={"contact": contact})


def product(request, pk):
    context = {
        "object": Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context)

