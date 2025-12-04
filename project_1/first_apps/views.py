from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("this is first apps home page")
    
def courses(request):
    return HttpResponse("this is courses page")
