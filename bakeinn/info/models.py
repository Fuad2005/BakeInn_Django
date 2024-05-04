from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Socials(models.Model):
    mail = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    facebook_link = models.CharField(max_length=100, default='', blank=True, null=True)
    instagram_link = models.CharField(max_length=100, default='', blank=True, null=True)
    whatsapp_link = models.CharField(max_length=100, default='', blank=True, null=True)
    youtube_link = models.CharField(max_length=100, default='', blank=True, null=True)
    linkedin_link = models.CharField(max_length=100, default='', blank=True, null=True)
    tiktok_link = models.CharField(max_length=100, default='', blank=True, null=True)
    twitter_link = models.CharField(max_length=100, default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Socials"


    def __str__(self):
        return "Socials"
    def save(self, *args, **kwargs):
        if not self.pk and Socials.objects.exists():
            raise ValidationError('There is can be only one Socials instance')
        return super(Socials, self).save(*args, **kwargs)