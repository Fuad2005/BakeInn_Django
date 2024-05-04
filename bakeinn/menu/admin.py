from django.contrib import admin
from .models import MenuItem, MenuItemImage
# Register your models here.

class MenuItemImageInline(admin.TabularInline):
    model = MenuItemImage
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemImageInline]

admin.site.register(MenuItem, MenuItemAdmin)