from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MenuItem
# Create your views here.

def menuPage(request):
    tag = request.GET.get('tag')
    if tag:
        menu_list = MenuItem.objects.filter(tag__title=tag)
    else:
        menu_list = MenuItem.objects.all()

    paginator = Paginator(menu_list, 12)

    page_number = request.GET.get('page')
    menu = paginator.get_page(page_number)

    return render(request, 'menu.html', {
        'menu' : menu
    })