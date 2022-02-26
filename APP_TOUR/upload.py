import os
from random import randint

def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_tour_upload_path(instance, filepath, app_name=None):
        
        filename, ext = get_name_ext(filepath)

        return f"tour/{instance.slug}/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"