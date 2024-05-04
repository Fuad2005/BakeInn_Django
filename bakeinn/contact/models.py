from django.db import models

# Create your models here.
class Contact(models.Model):
    SERVICE_CHOICES = [
        ('', 'Xidmətin növü'),
        ('tedbirlerin_teshkili', 'Tədbirlərin təşkili'),
        ('yerinde_istehsal_sistemi', 'Yerində istehsal sistemi'),
        ('seyyar_sistem', 'Səyyar sistem'),
        ('furshetler', 'Furşetlər'),
        ('banket_teshkili', 'Banket təşkili'),

    ]

    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='')
    message = models.TextField()


    def __str__(self):
        return self.name