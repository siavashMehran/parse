from django.db import models

from APP_GALLERY.upload import gallery_media_upload_path
from APP_TOUR.models import Tour

class Gallery(models.Model):
    
    title   = models.CharField(max_length=50)
    pic     = models.ImageField(upload_to=gallery_media_upload_path, null=True, blank=False,verbose_name='عکس')    


    def __str__(self):
        return f"{self.title}"

    class Meta:
        default_related_name = 'gallery'
    
    
    
class TourGallery(Gallery):
    class Meta:
        default_related_name = 'gallery'
        
    tour = models.ForeignKey(to=Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.name}"