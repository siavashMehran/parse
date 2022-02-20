
from .views import post_comment_for_blog
from django.urls import path

urlpatterns = [
    path('post-comment-blog/<str:slug>', post_comment_for_blog, name='post_comment_for_blogpost'),
]
