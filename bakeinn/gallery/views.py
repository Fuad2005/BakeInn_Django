from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GalleryItem
# Create your views here.
def galleryPage(request):
    gallery_list = GalleryItem.objects.all()

    paginator = Paginator(gallery_list, 12)
    page_number = request.GET.get('page')
    
    gallery = paginator.get_page(page_number)

    return render(request, 'gallery.html', {
        'gallery' : gallery
    })