from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    star_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    tag = models.ForeignKey('MenuCategory', related_name='menu_items', on_delete=models.CASCADE)


    
    def get_main_image_url(self):
        main_image = self.images.filter(main=True).first()
        if main_image and main_image.image:
            return main_image.image.url
        return '#'

    def __str__(self):
        return self.title



class MenuItemImage(models.Model):
    menu_item = models.ForeignKey(MenuItem, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu_items/')
    main = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.main:
            MenuItemImage.objects.filter(menu_item=self.menu_item, main=True).update(main=False)
        super().save(*args, **kwargs)




class MenuCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title