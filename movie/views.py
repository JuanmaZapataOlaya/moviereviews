from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welcome to Home Page</h1>')
    # return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Juan Manuel Zapata'})

def about(request):
    return HttpResponse('<h2> Estas en la pagina About</h2>')
