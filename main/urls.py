
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('modir/', admin.site.urls),

    path('', include('APP_INFO.urls')),
    path('tour', include('APP_TOUR.urls')),
    path('partials', include('partials.urls')),
]
