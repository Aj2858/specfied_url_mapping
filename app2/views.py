from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1> I am Student of Pyspiders</h1>')