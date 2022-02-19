
from .models import PostComment
from django.contrib import admin


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    ordering      = ['-timestamp']
    list_editable = ['is_offensive']
    list_display  = ['body', 'post', 'is_offensive']
    list_filter   = ['timestamp']
    list_per_page = 20