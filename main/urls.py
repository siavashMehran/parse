
from django.contrib import admin
from django.urls import path

from django.shortcuts import render
def home(request):

    return render(request, 'base/index.html', {}, status=200, content_type='text/html')
def about(request):

    return render(request, 'base/about.html', {}, status=200, content_type='text/html')


urlpatterns = [
    path('modir/', admin.site.urls),

    path('', home, name='home'),
    path('about', about, name='about'),
]
