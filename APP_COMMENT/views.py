
from .forms import PostCommentModelForm, ProductCommentModelForm
from .models import PostComment, ProductComment
from APP_BLOG.models import Post


def post_comment_for_blog(request, slug):
    
    post_instance   = Post.get_object_by_slug_or_404(slug)
    comment_instace = PostComment(post=post_instance)
    comment_form    = PostCommentModelForm(request.POST, instance=comment_instace)
    
    return comment_form.save_and_return_JSON_response()



