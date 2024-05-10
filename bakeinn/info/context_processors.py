from .models import Socials
from menu.models import MenuCategory
from info.models import HeaderFooterInfo

def add_socials_to_context(request):
    socials = Socials.objects.first()
    categories = MenuCategory.objects.all()
    header_footer_info = HeaderFooterInfo.objects.first()
    return {
            'socials': socials,
            'categories': categories,
            'header_footer_info': header_footer_info
            }