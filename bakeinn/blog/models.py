from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class BlogItem(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title