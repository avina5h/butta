from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text1 = "Welcome to the shop butta"
    return HttpResponse(text1)