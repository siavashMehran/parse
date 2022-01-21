from django.shortcuts import render

# Create your views here.


def partial_header(request):
    return render(request, 'partials/header.html', {})