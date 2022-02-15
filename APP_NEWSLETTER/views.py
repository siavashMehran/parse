from django.http import Http404
from django.shortcuts import redirect, render
from django.http.response import HttpResponseBadRequest
from django.urls import reverse
from APP_NEWSLETTER.froms import NewsletterModelForm

# Create your views here.

def subscribe(request):
    if request.method == "POST":
        newsletter_subscribe_form = NewsletterModelForm(request.POST)
        if newsletter_subscribe_form.is_validated_and_saved():
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect('404')