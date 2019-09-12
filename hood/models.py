from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class NeighbourHood(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=60)
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
     

class Business(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=60)
    email=models.EmailField(blank=True,null=True)
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    hoodbizID=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'Business-{self.name}'

class Occupant(models.Model):
    occupants_num=models.IntegerField(blank=True,default=0)
    hoodID=models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)


    def __str__(self):
        return f'Occupants-{self.occupants_num}-{self.hoodID.name}'


