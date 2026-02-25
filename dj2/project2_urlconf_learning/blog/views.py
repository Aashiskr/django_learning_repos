from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1>Hello, welcome to my blog!</h1>")
def About(request):
    a = 51
    return HttpResponse(f"This is the about page of my blog. The value of a is {a}.")

# Create your views here.
