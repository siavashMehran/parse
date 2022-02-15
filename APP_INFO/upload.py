
import os
from random import randint

def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_logo_upload_path(instance, filepath, app_name=None):
        
        filename, ext = get_name_ext(filepath)

        return f"logo/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"

def media_testimonial_upload_path(instance, filepath, app_name=None):
        
        filename, ext = get_name_ext(filepath)

        return f"testimonial/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"

def media_certificates_upload_path(instance, filepath, app_name=None):
        
        filename, ext = get_name_ext(filepath)

        return f"certificates/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"

def media_header_image_upload_path(instance, filepath, app_name=None):
        
        filename, ext = get_name_ext(filepath)

        return f"header_images/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"

