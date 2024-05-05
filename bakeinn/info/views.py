from django.shortcuts import render
from menu.models import MenuItem

# Create your views here.
def homePage(request):
    menu_items = MenuItem.objects.order_by('-id')[:5][::-1]

    return render(request, 'index.html', {
        'menu_items': menu_items
    })


def aboutPage(request):
    return render(request, 'about.html')

