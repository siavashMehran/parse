from django.http import HttpRequest
from django.shortcuts import render

from .models import FAQ, Certificates, PageHeaders, SiteSettings
from .forms import ContactUsModelForm

from django.utils.translation import get_language, activate



def home(request):
    
    return render(request, 'index.html', {}, status=200, content_type='text/html')


def about(request):

    certificates = Certificates.objects.all()
    site_settings = SiteSettings.get_latest()
    header_image = PageHeaders.objects.latest('pk').about_us_header_image

    context = {
        'certificates' : certificates,
        'short_story': site_settings.site_story_short,
        'about_img': site_settings.about_us_img,
        'header_image' : header_image,
    }
    return render(request, 'about.html', context, status=200, content_type='text/html')


def contact(request:HttpRequest):
    
    contact_us_form = ContactUsModelForm()
    header_image = PageHeaders.objects.latest('pk').contact_us_header_image
    faqs = FAQ.objects.all()

    if request.method == 'POST':
        contact_us_form.validate_and_save_POST_data(request.POST)
        contact_us_form = ContactUsModelForm()

    context = {
        'form' : contact_us_form, 
        'faqs':faqs, 
        'header_image': header_image
        }

    return render(request, 'contact.html', context)

    


