from django.shortcuts import render


def index(request):
    return render(request, 'usaunem/home.html')

# Create your views here.
