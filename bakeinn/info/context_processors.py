from .models import Socials

def add_socials_to_context(request):
    socials = Socials.objects.first()
    return {'socials': socials}