from .models import Post
from django.contrib import admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering     = ['-timestamp']
    list_display = ['title', 'author', 'views']

