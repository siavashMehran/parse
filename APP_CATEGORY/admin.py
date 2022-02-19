from django.contrib import admin
from .models import BlogPostCategory, TourCategory


@admin.register(TourCategory, BlogPostCategory)
class CategoryAdmin(admin.ModelAdmin):
    pass