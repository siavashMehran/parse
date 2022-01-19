from django.shortcuts import render

def tour_details(request):
    return render(request, 'tour-details.html', {})


def tour_list(request):
    return render(request, '', {})