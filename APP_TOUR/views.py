from django.shortcuts import render
from APP_CATEGORY.models import TourCategory
from APP_TOUR.models import Tour



def tour_list(request):
    categories = TourCategory.objects.all()


    context = {
        'categories' : categories
    }
    
    return render(request, 'tour_list.html', context)




def tour_by_category(request, category):
    categories = TourCategory.objects.all()


    context = {
        'categories' : categories
    }

    return render(request, 'tour_list.html', context)




def tour_details(request, slug):
    tour = Tour.objects.get(slug=slug)
    return render(request, 'tour_details.html', {})

