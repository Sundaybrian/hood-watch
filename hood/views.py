from django.shortcuts import render,get_list_or_404,redirect
from django.http import Http404,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse ("<h1>Hoodlum</h1>")
