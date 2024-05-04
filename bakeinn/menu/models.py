from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    star_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    tag = models.CharField(max_length=50)

    def get_first_image(menu_item):
        try:
            return menu_item.images.first().image.url
        except AttributeError:
            return None


class MenuItemImage(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_items/')
    order = models.IntegerField()
    
    class Meta:
        ordering = ['order']