
from django.db import models
from APP_BLOG.models import Post



class PostComment(models.Model):
    # relations
    post         = models.ForeignKey(to=Post, on_delete=models.CASCADE, blank=False)

    user_name    = models.CharField(max_length=50, blank=False)
    body         = models.TextField(max_length=300, blank=False, null=False)
    user_email   = models.EmailField(max_length=30, blank=True)
    #auto fields
    timestamp    = models.DateTimeField(auto_now_add=True)
    is_offensive = models.BooleanField(default=False)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name        = 'Comment-Post'
        verbose_name_plural = 'Comment-Post'
        default_related_name = 'comments'
    


class BadWords(models.Model):
    class Meta:
        verbose_name = 'کلمات رکیک'
        verbose_name_plural = 'کلمات رکیک'

    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word

    @classmethod
    def is_offensive(cls, string:str):
        bad_words = cls.objects.all()
        for word in bad_words:
            if word.word in string:
                return True
        
        return False


# ======== SIGNAL =========
# post save recieverfor <Comment> 
# this signal is a way to delete offensive comment for admin
# its an easier way around admin actions but with a boolean field
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=PostComment)
def pre_save_reciever(sender:PostComment, instance:PostComment, *args, **kwargs):
    if BadWords.is_offensive(instance):
        instance.is_offensive = True
        instance.save()