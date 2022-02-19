# django imports
from APP_CATEGORY.models import BlogPostCategory
from APP_COMMENT.forms import PostCommentModelForm
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

# models
from .models import Post

def blog_detail_view(request, postSlug):

    post_instance     = Post.get_object_by_slug_or_404(slug=postSlug)
    most_viewed_posts = Post.objects.all().order_by('views')[:4]
    comment_form      = PostCommentModelForm.get_comment_form_with_initial_or_blank(request.user)
    context = {
        'post'               :  post_instance,
        'form'               :  comment_form,
        'most_viewed_posts'  :  most_viewed_posts,
    }
    return render(request, 'blog_post_single.html', context)


class GenericBlogListView(ListView):
    # this class is just for being able to determine
    # if a page needs page number links at the bottom (pagination)
    class MyPaginator(Paginator):
        def more_than_one_page(self):
            return self.count > 1
            

    template_name = 'blog_list.html'
    context_object_name = 'page'
    ordering = ['-timestamp',]
    paginate_by = 12
    paginator_class = MyPaginator

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogPostCategory.objects.all()
        context['most_viewd'] = Post.objects.all().order_by('-views')
        context['object_list_count'] = self.get_queryset().count()
        return context



class BlogListByCategory(GenericBlogListView):
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['categorySlug'], is_active=True).order_by('-pk')

class BlogSearch(GenericBlogListView):
    paginate_by = 100
    def get_queryset(self):
        q = self.request.GET.get('q')
        return Post.search(q, ['-timestamp'])


def blog_detail_view(request, postSlug):

    return render(request, 'blog_detail.html')











# def blog_list_by_category(request, categorySlug):

#     posts = Post.objects.filter(category__slug=categorySlug, is_active=True)
#     categories = BlogPostCategory.objects.all()
#     latest_posts = Post.objects.all().order_by('-pk')[:3]

#     q = request.GET.get('q')      
#     paginator = Paginator(posts, 9)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)

#     return render(request, 'blog_list.html', {'posts':posts, 'categories':categories, 'latest_posts':latest_posts})

# def blog_search(request):

#     posts = Post.search(q, ['-timestamp'])
#     categories = BlogPostCategory.objects.all()
#     latest_posts = Post.objects.all().order_by('-pk')[:3]

#     q = request.GET.get('q')      
#     paginator = Paginator(posts, 9)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)
    
    
#     context = {
#         'paginator'    : paginator,
#         'posts'        : page_obj,
#         'page_number'  : page,
#         'categories'   : categories,
#         'latest_posts' : latest_posts
        
#     }
#     return render(request, 'blog_list.html', context)