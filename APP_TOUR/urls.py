from django.urls import path
from .views import tour_details
urlpatterns = [
   path('', tour_details, name='tourdetail') 
]
