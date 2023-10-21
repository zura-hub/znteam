from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import Item

def index(request):
    return render(request, 'main/index.html')

def service(request):
    return render(request, 'main/service.html')

def contact(request):
    return render(request, 'main/contact.html')


def display_items(request):
    items = Item.objects.all()
    return render(request, 'main/project.html', {'items': items})




def about(request):
    return render(request, 'main/about.html')
