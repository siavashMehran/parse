from django.urls.conf import path
from .views import BlogListByCategory, blog_detail_view, BlogSearch

urlpatterns = [
    path('category/<str:categorySlug>', BlogListByCategory.as_view(), name='blog_list_view'),
    path('posts/<str:postSlug>', blog_detail_view, name='blog_detail_view'),
    path('search', BlogSearch.as_view(), name='blog_search'),
]
