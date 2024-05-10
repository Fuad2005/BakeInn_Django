from django.shortcuts import render
from .models import ServiceItem
from django.core.paginator import Paginator

# Create your views here.
def servicePage(request):
    service = request.GET.get('service')
    if service:
        service_list = ServiceItem.objects.filter(title__icontains=service)
    else:
        service_list = ServiceItem.objects.all()

    paginator = Paginator(service_list, 8)
    page_number = request.GET.get('page')
    services = paginator.get_page(page_number)

    return render(request, 'services.html', {
        'services' : services
    })


def serviceDetail(request, id):
    service = ServiceItem.objects.get(id=id)
    recent = ServiceItem.objects.order_by('-id')[:6][::-1]

    return render(request, 'service_details.html', {
        'service': service,
        'recent': recent

    })