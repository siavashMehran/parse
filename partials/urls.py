
from django.urls import path
from .views import partial_header


urlpatterns = [
    path('header', partial_header, name='partial_header'),
]
