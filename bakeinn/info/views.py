from django.shortcuts import render
from menu.models import MenuItem
from service.models import ServiceItem

# Create your views here.
def homePage(request):
    menu_items = MenuItem.objects.order_by('-id')[:5][::-1]
    services = ServiceItem.objects.order_by('-id')[:8][::-1]

    return render(request, 'index.html', {
        'menu_items': menu_items,
        'services': services
    })


def aboutPage(request):
    return render(request, 'about.html')

