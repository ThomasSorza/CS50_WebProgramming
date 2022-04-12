from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/indes.html")

def thomas(request):
    return HttpResponse('Hello, Thoms!')

def arturo(request):
    return HttpResponse('Hi, Arturo')

def greet(request, name):
    return HttpResponse(f"Hello,{name.capitalize()}!")