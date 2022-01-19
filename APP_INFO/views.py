from django.shortcuts import render


from django.shortcuts import render
def home(request):
    return render(request, 'index.html', {}, status=200, content_type='text/html')


def about(request):
    return render(request, 'about.html', {}, status=200, content_type='text/html')
