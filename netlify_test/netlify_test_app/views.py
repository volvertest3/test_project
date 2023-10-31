from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def say_hello(request):
    return JsonResponse({"message": 'Hello World'})