from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


# Create your models here.
class NeighbourHood(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=60)
    occupants=models.IntegerField(blank=True,default=0)
    admin=models.ForeignKey(User,on_delete=models.DO_NOTHING)

class Business(models.Model):



class Occupants(models.Model):
    occupants=models.IntegerField(blank=True,default=0)
    hood=models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)


