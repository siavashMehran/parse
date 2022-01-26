from django.shortcuts import render

def tour_details(request, slug):
    return render(request, 'tour_details.html', {})


def tour_list(request):
    return render(request, 'tour_list.html', {})