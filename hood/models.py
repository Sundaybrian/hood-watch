from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Location(models.Model):
    locationName=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.locationName}-Location'

    def save_loc(self):  
        self.save() 

    def delete_loc(self):
        self.delete()     


class NeighbourHood(models.Model):
    hoodname=models.CharField(max_length=100)
    locations=models.ManyToManyField(Location)
    occupants=models.IntegerField(blank=True,default=0)
    admin=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.hoodname}'

    @classmethod
    def get_all_hoods(cls):
        hoods=cls.objects.all()
        return hoods


class Post(models.Model):
    '''  
    '''
    title=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to='posters/',default='')
    date_posted=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING,null=True,blank=True)


    def __str__(self):
        return f'Post-{self.title}'

    def get_absolute_url(self):
        '''

        '''  
        return reverse('post-detail',kwargs={'pk':self.pk})  

    def save_post(self):
        '''
        method to save a post
        '''
        self.save()

    @classmethod
    def get_posts(cls,hood_id):
        '''
        fetch all posts
        '''
        posts=cls.objects.filter(hood_id=hood_id).order_by('-date_posted')
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

    @classmethod
    def get_posts_by_username(cls,username):
        posts=cls.objects.filter(author=username).order_by('-date_posted')
        return posts


    @classmethod
    def delete_post(cls,post_id):

        '''
            method to delete a post
        '''

        post=cls.objects.get(id=post_id).delete()   

    @classmethod
    def search(cls,search_term):
        '''
        '''  
        posts=cls.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term) | Q(author__username__icontains=search_term))  
        return posts    
        

class Business(models.Model):
    businessname=models.CharField(max_length=100)
    businessemail=models.EmailField(blank=True,null=True)
    location=models.ForeignKey(Location,null=True,blank=True,on_delete=models.DO_NOTHING)
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING)
    image=models.ImageField(upload_to='business_posters/', default='')
    

    def get_absolute_url(self):
        '''

        '''  
        return reverse('business-detail',kwargs={'pk':self.pk})  


    def __str__(self):
        return f'Business-{self.businessname}'

    @classmethod
    def delete_business(cls,id):
        '''
        '''
        biz=cls.objects.get(id=id).delete()

    @classmethod
    def find_business(cls,business_id):
        '''
        '''  
        business=cls.objects.filter(Q(name__iexact=business_id) | Q(id=business_id) | Q(owner__username__icontains=business_id))  
        return business

    @classmethod
    def get_biz_by_username(cls,username):
        biznesses=cls.objects.filter(owner=username).all()
        return biznesses   



class Occupant(models.Model):
    occupants_num=models.IntegerField(blank=True,default=0)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)


    def __str__(self):
        return f'Occupants-{self.occupants_num}-{self.hood.name}'


