# django imports
from django.db import models
from django.http.response import Http404
from django.db.models.query_utils import Q

# third party modules
from tinymce import models as tinymce_models

# project related imports
from APP_CATEGORY.models import BlogPostCategory
from .upload import media_upload_path


class Post(models.Model):

    # Post data
    title  = models.CharField(blank=False, max_length=50, help_text='عنوان یا اسم پست', verbose_name='عنوان')
    summary = models.TextField('خلاصه', max_length=250, blank=False)
    image  = models.ImageField(blank=False, upload_to=media_upload_path, verbose_name='عکس')    
    body   = tinymce_models.HTMLField('متن', blank=False, max_length=2000)
    quote = models.TextField(max_length=500, blank=True)
    author = models.CharField(blank=True, max_length=40)
    is_active = models.BooleanField('فعال / غیر فعال', default=True)
    
    # categorizing
    category   = models.ForeignKey(to=BlogPostCategory, verbose_name='دسته', blank=True, on_delete=models.CASCADE)

    # auto fields
    timestamp  = models.DateTimeField("تاریخ و ساعت", auto_now_add=True)
    views      = models.IntegerField(blank=True, default=0, null=False, verbose_name='تعداد بازدید')
    slug       = models.SlugField(blank=True, allow_unicode=True, max_length=30, unique=True)

    def __str__(self) :
        return self.title

    def get_all_comments(self):
        return self.comments.all().order_by('-pk')

    def get_comments_count(self):
        return len(self.get_all_comments())

    def increment_views(self):
        pass
    @classmethod
    def get_object_by_slug_or_404(cls, slug):
        try    : post_instance = cls.objects.get(slug=slug)
        except : raise Http404('پاسخی برای درخواست شما وجود ندارد')
        return post_instance

    @classmethod
    def search(cls, querry, sorting:list=[]):
        condition =  Q(title__icontains=str(querry)) |  Q(summary__icontains=str(querry)) | Q(category__title__icontains=str(querry))
        qs = cls.objects.filter(condition, is_active=True).order_by('title').distinct()
        if sorting:
            return qs.order_by(*sorting)
        return qs

# ======== SIGNAL =========

# pre save reciever to slugify <Post>

from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Post)
def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.title.replace(' ', '-')

