from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1>Hello to my App</h1>")
def blog(response):
    return HttpResponse("<h2>this is a blog page</h2>")