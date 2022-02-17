from django.contrib import admin
from .models import TourCategory


@admin.register(TourCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass