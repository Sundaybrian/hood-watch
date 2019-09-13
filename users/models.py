from django.db import models
from django.contrib.auth.models import User
from hood.models import NeighbourHood,Business
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='naomi.jpg',upload_to='profile_pics')
    bio=models.TextField(blank=True)
    neighbourhood=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING,null=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'