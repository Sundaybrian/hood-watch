from django.shortcuts import render,get_list_or_404,redirect
from django.http import Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (UserPassesTestMixin,LoginRequiredMixin)
from django.views.generic import(ListView,DeleteView,DeleteView,CreateView,UpdateView,DetailView)
from django.contrib.auth.models import User
from .models import Business,NeighbourHood,Location,Post,ObjectDoesNotExist


# Create your views here.

def home(request):
    posts=Post.get_posts()

    return render(request,'hood/home.html',{'posts':posts})


class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
    template_name='hood/post-detail.html'


class PostCreateView(CreateView):
    model=Post
    template_name='hood/post-new.html'
    fields=['title','description','image']

    def form_valid(self,form):
        '''
        setting up the form instance user property to the current user before saving it
        '''
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name='hood/post-new.html'
    fields=['title','description','image']

    def form_valid(self,form):
        '''
        setting up the form instance user property to the current user before saving it
        '''
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
         fetch exact post check if current user is owner of the post
        '''
        post=self.get_object()
        
        if self.request.user==post.author:
            return True
        return False    






