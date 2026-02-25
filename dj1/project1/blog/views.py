from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello, welcome to my blog!")
def About(request):
    a=41+18
    return HttpResponse(f"This is the about page of my blog. The sum of 41 and 18 is {a}.")
# Create your views here.
