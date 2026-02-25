from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("Hello World")
def About(request):
    a=18+41
    return HttpResponse(f"This is about page hello ashish how are you lets be the best coder in this world {a}")

