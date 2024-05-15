from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MenuItem
from info.models import Socials
# Create your views here.

def menuPage(request):
    tag = request.GET.get('tag')
    title = request.GET.get('title')
    socials = Socials.objects.all()

    menu_list = MenuItem.objects.all()
    
    if tag:
        menu_list = MenuItem.objects.filter(tag__title=tag)

    if title:
        menu_list = MenuItem.objects.filter(title__icontains=title)
   

    paginator = Paginator(menu_list, 12)

    page_number = request.GET.get('page')
    menu = paginator.get_page(page_number)

    return render(request, 'menu.html', {
        'menu' : menu,
        'socials': socials
    })


def menuDetail(request, id):
    menu = MenuItem.objects.get(id=id)
    recent = MenuItem.objects.order_by('-id')[:5][::-1]

    return render(request, 'menu_details.html', {
        'menu': menu,
        'recent': recent

    })