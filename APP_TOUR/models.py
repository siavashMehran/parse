import imp
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from tinymce.models import HTMLField
from APP_CATEGORY.models import TourCategory



class Tour(models.Model):

    transports = (
        ('aeropalne', 'هواپیما'),
        ('bus', 'اتوبوس'),
        ('van', 'ون'),
        ('car', 'سواری'),
        (None, 'ندارد'),
    )

    class Meta:
        verbose_name = 'تور'
        verbose_name_plural = 'تور ها'

    def __str__(self):
        return self.name


    name = models.CharField('اسم تور', max_length=100, blank=False)
    city = models.CharField('شهر مقصد', max_length=18)
    caption = models.CharField('توضیحات کوتاه', max_length=120, blank=False)
    description = HTMLField('توضیحات کوتاه', blank=False)
    duration = models.CharField('مدت اقامت', max_length=80, blank=False)
    slug = models.SlugField(blank=True, allow_unicode=True, max_length=30, unique=True)
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    transport_type = models.CharField('نوع ترانسفر', max_length=30, blank=True, null=True, choices=transports)
    


    @property
    def has_residence(self):
        return self.residence == None

    @property
    def price(self):
        return f"{20000000:,}"





class Residence(models.Model):

    class Meta:
        verbose_name = 'اقامتگاه'
        verbose_name_plural = 'اقامتگاه'
        default_related_name = 'residence'

    tour = models.OneToOneField(Tour, on_delete=models.CASCADE)
    name = models.CharField('نام محل', max_length=80, blank=False)
    rating = models.IntegerField('ستاره', blank=True)
    room_service = models.TextField('روم سرویس', max_length=400, blank=True)
    



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



class TourService(models.Model):

    class Meta:
        verbose_name = 'خدمات تور'
        verbose_name_plural = 'خدمات تور'
        default_related_name = 'tour_services'

    name = models.CharField('نام سرویس', max_length=50, blank=False)
    price = models.IntegerField('قیمت به ریال')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)






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


