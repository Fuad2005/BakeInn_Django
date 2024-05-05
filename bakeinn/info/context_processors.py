from .models import Socials
from menu.models import MenuCategory

def add_socials_to_context(request):
    socials = Socials.objects.first()
    categories = MenuCategory.objects.all()
    return {
            'socials': socials,
            'categories': categories
            }