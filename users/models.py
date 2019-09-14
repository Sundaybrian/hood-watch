from django.db import models
from django.contrib.auth.models import User
from hood.models import NeighbourHood,Business,Location
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='naomi.jpg',upload_to='profile_pics')
    bio=models.TextField(blank=True)
    neighbourhood=models.ForeignKey(NeighbourHood,on_delete=models.DO_NOTHING,null=True)
    location=models.ForeignKey(Location,on_delete=models.DO_NOTHING,null=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        '''
        overriding the save method inorder to resize the profile images
        '''

        super(Profile,self).save(*args,**kwargs)
        img=Image.open(self.image)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)    

