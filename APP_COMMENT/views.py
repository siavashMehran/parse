
from django.shortcuts import redirect
from django.urls import reverse
from .forms import PostCommentModelForm
from .models import PostComment
from APP_BLOG.models import Post

def post_comment_for_blog(request, slug):
    post_instance   = Post.get_object_by_slug_or_404(slug)
    comment_instace = PostComment(post=post_instance)
    comment_form    = PostCommentModelForm(request.POST, instance=comment_instace)
    if comment_form.is_valid():
        comment_form.save()
    return redirect(reverse('blog_detail_view', args=[slug]))


