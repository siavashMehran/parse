

from django.shortcuts import render


def response_404(request):
    return render(request, "404.html")