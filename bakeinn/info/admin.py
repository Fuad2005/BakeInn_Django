from django.contrib import admin
from .models import Socials, HeaderFooterInfo, HomePageText, AboutPageText, Faq
# Register your models here.

admin.site.register(Socials)
admin.site.register(HeaderFooterInfo)
admin.site.register(HomePageText)
admin.site.register(AboutPageText)
admin.site.register(Faq)