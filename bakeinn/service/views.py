from django.shortcuts import render
from .models import ServiceItem
from django.core.paginator import Paginator

# Create your views here.
def servicePage(request):
    service_list = ServiceItem.objects.all()
    paginator = Paginator(service_list, 8)
    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)

    return render(request, 'services.html', {
        'services' : services
    })