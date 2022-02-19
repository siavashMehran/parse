
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from .responses import response_404

urlpatterns = [
    
]


urlpatterns = i18n_patterns(
    path('404/', response_404, name='404'),
    path('modir/', admin.site.urls),

    path('', include('APP_INFO.urls')),

    path('tour/', include('APP_TOUR.urls')),
    path('newsletter/', include('APP_NEWSLETTER.urls')),
    path('blog/', include('APP_BLOG.urls')),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)