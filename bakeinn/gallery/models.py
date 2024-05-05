from django.db import models

# Create your models here.
class GalleryItem(models.Model):
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return 'Image ' + str(self.id)