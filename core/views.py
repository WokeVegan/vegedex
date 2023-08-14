from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


# Create your views here.
def about(request):
    return render(request, 'core/about.html')


# Create your views here.
def login(request):
    return render(request, 'core/login.html')


# Create your views here.
def register(request):
    return render(request, 'core/register.html')


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def handler404(request, exception):
    return render(request, 'core/404.html')
