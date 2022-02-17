from django.urls import path
from .views import tour_by_category, tour_details, tour_list
urlpatterns = [
   path('', tour_list, name='tours'),
   path('categories/<str:category>', tour_by_category, name='tour_category_view'),
   path('<str:slug>', tour_details, name='tourdetail'),
]
