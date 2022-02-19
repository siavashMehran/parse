from django.shortcuts import render
from APP_CATEGORY.models import BlogPostCategory

from APP_INFO.models import PageHeaders, SiteSettings

# Create your views here.


def partial_header(request):
    logo = SiteSettings.objects.latest('pk').site_logo
    blog_categories = BlogPostCategory.objects.all()
    return render(request, 'partials/header.html', {'logo':logo, 'blog_categories' : blog_categories})

def partial_banner(request, *args, **kwargs):
    banner_images = PageHeaders.objects.latest('pk')
    paths = {
        'blog' : ('بلاگ', banner_images.blog_header_image ),
        'about' : ('درباره ما', banner_images.about_us_header_image ),
        'tour' : ('تور ها', banner_images.tour_header_image ),
        'contact' : ('تماس با ما', banner_images.contact_us_header_image),
        '' : ('', banner_images.about_us_header_image)
    }
    banner_data = paths.get(args[0], '')
    return render(request, 'partials/banner.html', {'banner_path': banner_data[0], 'banner_image': banner_data[1]})