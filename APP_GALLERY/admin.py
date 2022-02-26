from django.contrib import admin

from APP_GALLERY.models import TourGallery

# Register your models here.
class TourGalleryTabularAdmin(admin.TabularInline):
    
    model = TourGallery
    extra = 2