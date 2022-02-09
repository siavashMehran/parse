

from django.urls import path
from .views import about, home, contact


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
