from django.shortcuts import render
from .models import MenuItem
# Create your views here.

def menuPage(request):
    menu = MenuItem.objects.all()

    return render(request, 'menu.html', {
        'menu' : menu
    })