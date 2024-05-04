from django.shortcuts import render, redirect
from .forms import ContactForm
from info.models import Socials

# Create your views here.
def contactPage(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()



    socials = Socials.objects.first()
    return render(request, 'contact.html', {
        'form' : form,
        'socials' : socials
    })



