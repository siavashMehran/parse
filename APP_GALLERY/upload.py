import os
from random import randint


def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def gallery_media_upload_path(instance, filepath):
        """
        example : `gallery/5_43848283138283.jpeg`
        """
        filename, ext = get_name_ext(filepath)
        return f"gallery/{randint(1, 10)}_{randint(100000000000, 999999999999999)}{ext}"
        
