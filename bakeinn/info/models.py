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
    

class HeaderFooterInfo(models.Model):
    header_logo = models.ImageField(upload_to='header_footer/')
    footer_logo = models.ImageField(upload_to='header_footer/')
    footer_text = models.TextField()

    def __str__(self):
        return "Header Footer Info"
    
    def save(self, *args, **kwargs):
        if not self.pk and HeaderFooterInfo.objects.exists():
            raise ValidationError('There is can be only one HeaderFooterInfo instance')
        return super(HeaderFooterInfo, self).save(*args, **kwargs)

class HomePageText(models.Model):
    banner_mini_text = models.CharField(max_length=100)
    banner_bold_text = models.CharField(max_length=100)
    banner_main_text = models.TextField()
    about_bold_text = models.CharField(max_length=100)
    about_main_text = models.TextField()
    number_of_clients = models.IntegerField()
    experience_years = models.IntegerField()
    clean_percent = models.IntegerField(default=100, blank=True, null=True)
    number_of_members = models.IntegerField()

    def __str__(self):
        return "Home Page Texts"
    
    def save(self, *args, **kwargs):
        if not self.pk and HomePageText.objects.exists():
            raise ValidationError('There is can be only one HomePageText instance')
        return super(HomePageText, self).save(*args, **kwargs)
    

class AboutPageText(models.Model):
    about_bold_text = models.CharField(max_length=100)
    about_main_text = models.TextField()

    def __str__(self):
        return "About Page Text"
    
    def save(self, *args, **kwargs):
        if not self.pk and AboutPageText.objects.exists():
            raise ValidationError('There is can be only one AboutPageText instance')
        return super(AboutPageText, self).save(*args, **kwargs)
    

class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question