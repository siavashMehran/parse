
from django.contrib import admin

from APP_GALLERY.admin import TourGalleryTabularAdmin
from .models import Residence, Tour, TourService
# Register your models here.


class ResidenceStackedAdmin(admin.StackedInline):
    model = Residence
    extra = 1

class TourServiceTubularAdmin(admin.StackedInline):
    model = TourService
    extra = 1
    exclude = ['is_selected']

# @admin.register(Residence)
# class ResidenceAdmin(admin.ModelAdmin):
#     inlines = [ResidenceDoubleFieldTubularAdmin]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [ResidenceStackedAdmin, TourServiceTubularAdmin, TourGalleryTabularAdmin]

