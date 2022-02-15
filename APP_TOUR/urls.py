from django.urls import path
from .views import tour_details, tour_list
urlpatterns = [
   path('', tour_list, name='tours'),
   path('<str:slug>', tour_details, name='tourdetail'),
]
