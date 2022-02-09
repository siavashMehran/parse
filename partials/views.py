from django.shortcuts import render

from APP_INFO.models import SiteSettings

# Create your views here.


def partial_header(request):
    logo = SiteSettings.objects.latest('pk').site_logo
    return render(request, 'partials/header.html', {'logo':logo})