from django.shortcuts import render
from .models import BlogItem
from django.core.paginator import Paginator
from menu.models import MenuCategory


# Create your views here.
def blogPage(request):
    blog_items = BlogItem.objects.all()
    
    title = request.GET.get('title')
    if title:
        blog_items = blog_items.filter(title__icontains=title)

    recent = BlogItem.objects.all().order_by('-created_at')[:3]

    page = request.GET.get('page')
    paginator = Paginator(blog_items, 3)

    blog_items = paginator.get_page(page)

    categories = MenuCategory.objects.all()

    return render(request, 'blogs.html', {
        'blog_items': blog_items,
        'categories': categories,
        'recent': recent
    })



def blogDetail(request, blog_id):
    blog_item = BlogItem.objects.get(pk=blog_id)
    recent = BlogItem.objects.all().order_by('-created_at')[:3]
    categories = MenuCategory.objects.all()

    return render(request, 'blog_detail.html', {
        'blog_item': blog_item,
        'categories': categories,
        'recent': recent
    })