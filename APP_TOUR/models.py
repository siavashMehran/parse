import imp
import math
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.http import Http404
from tinymce.models import HTMLField
from APP_CATEGORY.models import TourCategory
from APP_TOUR.upload import media_tour_upload_path
from django.core.files.images import ImageFile
from io import BytesIO

class Tour(models.Model):

    transports = (
        ('هواپیما', 'هواپیما'),
        ('اتوبوس', 'اتوبوس'),
        ('ون', 'ون'),
        ('سواری', 'سواری'),
        (None, 'ندارد'),
    )

    class Meta:
        verbose_name = 'تور'
        verbose_name_plural = 'تور ها'

    def __str__(self):
        return self.name

    plan = models.ImageField(upload_to=media_tour_upload_path, default=ImageFile(BytesIO()))
    image = models.ImageField(upload_to=media_tour_upload_path, default=ImageFile(BytesIO()))

    name = models.CharField('اسم تور', max_length=100, blank=False)
    city = models.CharField('شهر مقصد', max_length=18)
    caption = models.CharField('توضیحات کوتاه', max_length=120, blank=False)
    features = models.CharField('ویزگی های کلیدی', max_length=120, help_text='مثال : تور لیدر - غذای محلی - کنسرت زنده')
    description = HTMLField('توضیحات کوتاه', blank=False)
    duration = models.CharField('مدت اقامت', max_length=80, blank=False)
    slug = models.SlugField(blank=True, allow_unicode=True, max_length=30, unique=True)
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE, verbose_name='دسته بندی')
    transport_type = models.CharField('نوع ترانسفر', max_length=30, blank=True, null=True, choices=transports)
    price = models.PositiveIntegerField('قیمت پایه')
    has_leader = models.BooleanField('تور لیدر', default=True)

    @property
    def has_residence(self):
        if hasattr(self, 'residence'):
            return self.residence != None
        return False

    def get_gallery_or_none(self):
        if hasattr(self, 'gallery'):
            return self.gallery.all()
        return None

    def get_residence_or_none(self):
        if hasattr(self, 'residence'):
            return self.residence
        return None

    @property
    def get_price(self):
        initial_price = self.price
        if self.has_residence:
            initial_price += self.residence.price
        
        return math.ceil(initial_price + (initial_price * .05))

    @property
    def pretty_price(self):
        return f"{self.get_price:,}"

    @classmethod
    def get_by_slug_or_404(cls, slug):
        try:
            return cls.objects.get(slug=slug)
        except:
            raise Http404



class Residence(models.Model):

    class Meta:
        verbose_name = 'اقامتگاه'
        verbose_name_plural = 'اقامتگاه'
        default_related_name = 'residence'

    tour = models.OneToOneField(Tour, on_delete=models.CASCADE)
    name = models.CharField('نام محل', max_length=80, blank=False)
    rating = models.IntegerField('ستاره', blank=True, null=True)
    room_service = models.TextField('روم سرویس', max_length=400, blank=True)
    price = models.PositiveIntegerField('قیمت به ریال')



    # booleans
    parking = models.BooleanField('پارکینگ دارد', default=False)
    food   = models.BooleanField('غذا دارد', default=False)
    wifi   = models.BooleanField('wi-fi', default=False)
    tv     = models.BooleanField('تلویزیون', default=False)
    aircon = models.BooleanField('سیستم تهویه', default=False)


    def room_service_table(self):
        rows = self.room_service.splitlines()
        cleaned_rows = [x for x in rows if x != '']
        splited = []
        for row in cleaned_rows:
            splited.append(row.split('='))
        return [[x.lstrip().rstrip(), y.lstrip().rstrip()] for x, y in splited]

    def rating_as_iterable(self):
        return range(self.rating)
    def __str__(self):
        return f"{self.name}"

class TourService(models.Model):

    class Meta:
        verbose_name = 'خدمات تور'
        verbose_name_plural = 'خدمات تور'
        default_related_name = 'services'

    name = models.CharField('نام سرویس', max_length=50, blank=False)
    price = models.PositiveIntegerField('قیمت به ریال')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"



# 
# denceDubleField(models.Model):
#     name = models.CharField('نام فیلد', max_length=80, blank=False)
#     value = models.CharField('مقدار فیلد', max_length=80, blank=True)
#     icon = models.CharField('ایکون', max_length=80, blank=True, default='ss')
#     residence = models.ForeignKey(Residence, on_delete=models.CASCADE)





###################################
############## SIGNALS ############
###################################

def set_slug(sender, instance):
    generated_slug = instance.name.replace(' ', '-')
    if (not instance.slug):
        # checks to see if the slug is unique and set the slug fild, pre_save
        while sender.objects.filter(slug=generated_slug).exists():
            increment = 1
            generated_slug = f"{generated_slug}{increment}"
            increment += 1
        instance.slug = generated_slug[:29] # this slicing is because max_length for slugField is 30
    else:
        instance.slug = instance.slug.strip()[:29]



@receiver(pre_save, sender=Tour)
def pre_save_reciever(sender, instance, *args, **kwargs):
    set_slug(sender, instance)


