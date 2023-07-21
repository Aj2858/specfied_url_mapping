from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1> Welcome to Bihar')

def second(request):
    return HttpResponse('<h1><marquee>Wlcome to Gujarat<marquee></h1>')
