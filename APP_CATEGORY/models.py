from django.db import models
from django.http.response import Http404
from django.urls.base import reverse


class Category(models.Model):
    

    title = models.CharField(max_length=60)
    slug  = models.CharField(max_length=60, blank=True)

    class Meta:
            verbose_name = 'دسته'
            verbose_name_plural = 'دسته بندی ها'
            default_related_name = 'categories'
            abstract = True
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        # return reverse("category_page", kwargs={"category": self.slug})
        raise NotImplementedError

    @classmethod
    def get_object_by_slug_or_404(cls, slug):
        try    : category = cls.objects.get(slug=slug)
        except : raise Http404('صفحه مورد نظر پیدا نشد 404')
        return category




class TourCategory(Category):
    pass












###################################
############## SIGNALS ############
###################################

from random import randint 
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=TourCategory)
def pre_save_reciever(sender, instance, *args, **kwargs):
    generated_slug = instance.title.replace(' ', '-')
    if (not instance.slug) or (instance.slug != generated_slug):
        # checks to see if the slug is unique and set the slug fild, pre_save
        while sender.objects.filter(slug=generated_slug).exists():
            generated_slug = f"{generated_slug}-{randint(1, 10)}"
        instance.slug = generated_slug
    del generated_slug
        
