
from .views import post_comment_for_blog, post_comment_for_product
from django.urls import path

urlpatterns = [
    path('post-comment-blog/<str:slug>', post_comment_for_blog, name='post_comment_blog_page'),
    path('post-comment-product/<str:slug>', post_comment_for_product, name='post_comment_product_page'),
]
