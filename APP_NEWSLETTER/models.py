from django.db import models

# Create your models here.


class NewsletterClient(models.Model):

    class Meta:
        verbose_name = 'عضو'
        verbose_name_plural = 'اعضا'
    
    email = models.EmailField('ایمیل', primary_key=True, unique=True, blank=False, max_length=40)

    def __str__(self):
        return self.email


    