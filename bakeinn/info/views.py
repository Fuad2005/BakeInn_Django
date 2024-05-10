from django.shortcuts import render
from menu.models import MenuItem
from service.models import ServiceItem
from .models import HomePageText, AboutPageText, Faq

# Create your views here.
def homePage(request):
    menu_items = MenuItem.objects.order_by('-id')[:5][::-1]
    services = ServiceItem.objects.order_by('-id')[:8][::-1]
    home_page_text = HomePageText.objects.first()

    return render(request, 'index.html', {
        'menu_items': menu_items,
        'services': services,
        'home_page_text': home_page_text
    })


def aboutPage(request):
    about_page_text = AboutPageText.objects.first()
    number_values = HomePageText.objects.values('number_of_clients', 'experience_years', 'clean_percent', 'number_of_members').first()
    faqs = Faq.objects.all()

    return render(request, 'about.html', {
        'about_page_text': about_page_text,
        'faqs': faqs,
        'number_values': number_values
    })

