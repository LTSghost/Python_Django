from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def TemIndex(request):
    return render(request, 'index.html')


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.<h1>")
