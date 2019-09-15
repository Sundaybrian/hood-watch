from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (UserPassesTestMixin,LoginRequiredMixin)
from django.views.generic import(ListView,DeleteView,DeleteView,CreateView,UpdateView,DetailView)
from django.contrib.auth.models import User
from hood.models import *
from users.models import Profile



# Create your views here.
@login_required
def home(request):
    posts=Post.get_posts()

    return render(request,'hood/home.html',{'posts':posts})


class UserPostListView(ListView):
    '''
    class view to display a single user posts
    '''
    model=Post
    context_object_name='posts'
    template_name='hood/user-posts.html'
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        '''
        grab the post author and fetch their posts
        '''
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.get_posts_by_username(user)


class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
    template_name='hood/post-detail.html'


class PostCreateView(SuccessMessageMixin,CreateView):
    model=Post
    template_name='hood/post-new.html'
    fields=['title','description','image']
    success_message = "%(title)s was created successfully"


    def form_valid(self,form):
        '''
        setting up the form instance user property to the current user before saving it
        '''
        form.instance.author=self.request.user
        form.instance.hood=self.request.user.profile.neighbourhood
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model=Post
    template_name='hood/post-new.html'
    fields=['title','description','image']
    success_message = "%(title)s was updated successfully"


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


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    '''
    view to delete a post
    '''
    model=Post
    template_name='hood/post-delete.html'
    context_object_name='post'
    success_url='/'

    def test_func(self):

        '''
            fetch exact post check if current user is owner of the post
        '''
        post=self.get_object()

        if self.request.user==post.author:
            return True
        return False 


class BusinessCreateView(SuccessMessageMixin,CreateView):
    model=Business
    template_name='hood/new-biz.html'
    fields=['businessname','businessemail','image']
    success_message = "%(businessname)s was created successfully"
   

    def form_valid(self,form):
        '''
        setting up the form instance user property to the current user before saving it
        '''
        form.instance.owner=self.request.user
        form.instance.hood=self.request.user.profile.neighbourhood
        return super().form_valid(form)

class BusinessUpdateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    model=Business
    template_name='hood/new-biz.html'
    fields=['businessname','businessemail','image']
    success_message = "%(businessname)s was updated successfully"


    def form_valid(self,form):
        '''
        setting up the form instance user property to the current user before saving it
        '''
        form.instance.owner=self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
         fetch exact business check if current user is owner of the business
        '''
        biz=self.get_object()

        if self.request.user==biz.owner:
            return True
        return False   




class BusinessDetailView(DetailView):
    model=Business
    context_object_name='biz'
    template_name='hood/business-detail.html'



class UserBusinessListView(ListView):
    '''
    class view to display a single user posts
    '''
    model=Business
    context_object_name='biznesses'
    template_name='hood/user-biznesses.html'
    paginate_by=5

    def get_queryset(self):
        '''
        grab the business owner and fetch their businesses
        '''
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Business.get_biz_by_username(user)


def business(request):
    '''
    view function to display businesses of a particular neighbourhood
    '''
    profile=Profile.objects.get(user__username=request.user)
    business=Business.objects.filter(hood_id=profile.neighbourhood_id).all()

    return render(request,'hood/business.html',{'business':business,'profile':profile})













