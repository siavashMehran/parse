import os
from random import randint
def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext


def upload(app_name:str):

    def media_upload_path(instance, filepath):
        
        filename, ext = get_name_ext(filepath)

        return f"{app_name}/{randint(1, 10)}_{randint(100000000000, 999999999999999)}.{ext}"

    return media_upload_path