from django.shortcuts import render
from APP_CATEGORY.models import TourCategory
from APP_TOUR.models import Tour


from django.db import connection, reset_queries
import time
from functools import wraps
def querry_debuger(func):
    @wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        start_q = len(connection.queries)
        start_t = time.perf_counter()

        result = func(*args, **kwargs)

        stop_t = time.perf_counter()
        stop_q = len(connection.queries)
        print()
        print(f" === {func.__name__}  ===")
        print(f'number of querries :{stop_q - start_q}')
        print(f'time taken         :{stop_t - start_t:.2f}')
        print()
        # for querry in connection.queries:
        #     print(querry)
        #     print()
        print()
        return result
    return inner_func


def tour_list(request):
    categories = TourCategory.objects.all()


    context = {
        'categories' : categories
    }
    
    return render(request, 'tour_list.html', context)


@querry_debuger
def tour_by_category(request, category):
    categories = TourCategory.objects.all()
    tours = Tour.objects.filter(category__slug=category).prefetch_related('residence')


    context = {
        'categories' : categories,
        'tours' : tours
    }

    return render(request, 'tour_list.html', context)



@querry_debuger
def tour_details(request, slug):
    tour = Tour.get_by_slug_or_404(slug=slug)
    tour_gallery = tour.get_gallery_or_none()
    residence = tour.get_residence_or_none()
    tour_services = tour.services.all()
    print()
    print()
    print()
    print(request.POST)
    print()
    print()
    context = {
        'tour' : tour,
        'gallery' : tour_gallery,
        'residence' : residence,
        'services' : tour_services,
    }
    return render(request, 'tour_details.html', context)

