from django.shortcuts import render,get_list_or_404,redirect
from django.http import Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (UserPassesTestMixin,LoginRequiredMixin)
from django.views.generic import(ListView,DeleteView,DeleteView,CreateView,UpdateView)
from django.contrib.auth.models import User
from .models import Business,NeighbourHood,Location,Post,ObjectDoesNotExist


# Create your views here.

def home(request):
    return render(request,'hood/home.html')
