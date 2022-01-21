from django.shortcuts import render
from .forms import ContactUsModelForm

from django.shortcuts import render
def home(request):
    return render(request, 'index.html', {}, status=200, content_type='text/html')


def about(request):
    return render(request, 'about.html', {}, status=200, content_type='text/html')


def ContactUs(request):
    contact_us_form = ContactUsModelForm()
    if request.METHOD == 'POST': contact_us_form.validate_and_save_POST_data(request.POST)
    return render(request,  {'form' : contact_us_form})

    


