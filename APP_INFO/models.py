
from django.db import models

# imports for signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.core.files.images import ImageFile
from io import FileIO

# media files upload path
from .upload import (
    media_certificates_upload_path, 
    media_logo_upload_path, 
    media_testimonial_upload_path,
    media_header_image_upload_path,
    )


class SiteSettings(models.Model):

    # to keep help texts more organized
    help_text = {
        'logo'         : '80 x 110 image',
        'cell'         : 'Example : +98 939 005 2349',
        'phone'        : 'Example : +98 263 260 7383',
        'address'      : 'Example : طهران - ونک - خیابان چهارم - ساختمان ما',
        'story_short'  : 'معرفی کوتاه',
        'story_long'   : 'داستان ما',
    }


    # site header
    site_logo    = models.ImageField(upload_to=media_logo_upload_path, blank=False)

    # contacting info
    site_email   = models.EmailField(max_length=40, blank=False)
    site_phone   = models.CharField(max_length=20, blank=False, help_text=help_text['phone'])
    site_cell    = models.CharField(max_length=20, blank=False, help_text=help_text['cell'])
    site_address = models.CharField(max_length=200, blank=False, help_text=help_text['address'])

    # about us
    site_story_short = models.TextField(max_length=300, blank=False, help_text=help_text['story_short'])
    site_story_long  = models.TextField(max_length=900, blank=False, help_text=help_text['story_long'])
    about_us_img = models.ImageField(upload_to=media_logo_upload_path, blank=False)

    def __str__(self):
        return 'Main Configuration'

    @classmethod
    def get_latest(cls):
        return cls.objects.latest('pk')

    class Meta:
        verbose_name = 'اطلاعات اصلی'
        verbose_name_plural = 'اطلاعات اصلی'

# ======== SIGNAL  =========

# pre save reciever for <SiteSettings> 
@receiver(pre_save, sender=SiteSettings)
def pre_save_reciever(sender:SiteSettings, instance, *args, **kwargs):
    if sender.objects.count() > 0 :
        sender.objects.all().delete()








# contact us form
class ContactUs(models.Model):

    help_text = {
        'user_name'  : 'نام مشتری',
        'user_contact_info'   : 'اطلاعات تماس مشتری شماره ایمیل یا . . . ',
        'title'   : 'موضوع پیام',
        'message'   : 'پیام',
    }

    user_name  = models.CharField(max_length=40, blank=True, help_text=help_text['user_name'])
    user_contact_info = models.CharField(max_length=50, blank=True, help_text=help_text['user_contact_info'])
    title      = models.CharField(max_length=60, blank=True, help_text=help_text['title'])
    message    = models.TextField(max_length=300, blank=False, help_text=help_text['message'])

    def __str__(self):
        return self.title or 'Untitled Message !'

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'



class Testimonial(models.Model):

    # to keep help texts more organized
    help_text = {
        'tour_loc'  :  'تور کجا',
        'image'  :  '300 x 400',
        'story' : 'تجربه از سفر'
    }


    name    = models.CharField(max_length=40, blank=False)
    tour_loc   = models.CharField(max_length=40, blank=False, help_text=help_text['tour_loc'])
    image   = models.ImageField(upload_to=media_testimonial_upload_path, blank=True, help_text=help_text['image'])
    story = models.TextField(max_length=300, blank=False)


    def __str__(self) :
        return f'{self.name} {self.title}'

    class Meta:
        verbose_name = 'حرف مشتری'
        verbose_name_plural = 'حرف های مشتریان'


class Certificates(models.Model):

    class Meta:
        verbose_name = 'گواهینامه ها'
        verbose_name_plural = 'گواهینامه'

    name = models.CharField('نام مدرک', max_length=60, blank=False)
    img = models.ImageField(upload_to=media_certificates_upload_path, blank=False)
    caption = models.TextField('توضیح', blank=False)

    def __str__(self):
        return self.name



class FAQ(models.Model):

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question

    question = models.CharField('سوال', max_length=300, blank=False)
    answer = models.TextField('جواب', blank=False, max_length=400)

class PageHeaders(models.Model):

    contact_us_header_image = models.FileField('تصویر هدر صفحه تماس با ما', upload_to=media_header_image_upload_path, blank=False)
    about_us_header_image = models.FileField('تصویر هدر صفحه درباره ما', upload_to=media_header_image_upload_path, blank=False)
    tour_header_image = models.FileField('تصویر هدر صفحه تور ها', upload_to=media_header_image_upload_path, blank=False)
    blog_header_image = models.FileField('تصویر هدر صفحه بلاگ', upload_to=media_header_image_upload_path, blank=False)

    def __str__(self):
        return 'Pages Header Images'
    