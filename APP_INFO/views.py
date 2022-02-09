from django.http import HttpRequest
from django.shortcuts import render

from .models import FAQ, Certificates, SiteSettings
from .forms import ContactUsModelForm

from django.utils.translation import get_language, activate



def home(request):

    # try:
    #     activate(get_language())
    return render(request, 'index.html', {}, status=200, content_type='text/html')


def about(request):

    certificates = Certificates.objects.all()
    site_settings = SiteSettings.get_latest()
    context = {
        'certificates' : certificates,
        'short_story': site_settings.site_story_short,
        'about_img': site_settings.about_us_img,
    }
    return render(request, 'about.html', context, status=200, content_type='text/html')


def contact(request:HttpRequest):
    
    contact_us_form = ContactUsModelForm()
    faqs = FAQ.objects.all()

    if request.method == 'POST':
        contact_us_form.validate_and_save_POST_data(request.POST)
        print(request.POST)


    context = {'form' : contact_us_form, 'faqs':faqs}
    return render(request, 'contact.html', context)

    


