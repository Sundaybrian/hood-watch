from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}-Location'

class NeighbourHood(models.Model):
    name=models.CharField(max_length=100)
    location=models.ForeignKey(Location,blank
    =True,null=True,on_delete=models.DO_NOTHING)
    occupants=models.IntegerField(blank=True,default=0)
    admin=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Hood-{self.name}'

class Post(models.Model):
    '''  
    '''
    title=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'Post-{self.title}'

    def save_post(self):
        '''
        method to save a post
        '''
        self.save()

    @classmethod
    def get_posts(cls):
        '''
        fetch all posts
        '''
        posts=cls.objects.order_by('-date_posted')
        return posts

    @classmethod
    def get_post_by_id(cls,id):
        '''
        fetch a post by its id
        '''
        try:
            post=cls.objects.get(id=id)
            
        except ObjectDoesNotExist:
            raise Http404()
            assert False
            



     

class Business(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(blank=True,null=True)
    location=models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'Business-{self.name}'

class Occupant(models.Model):
    occupants_num=models.IntegerField(blank=True,default=0)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)


    def __str__(self):
        return f'Occupants-{self.occupants_num}-{self.hood.name}'


