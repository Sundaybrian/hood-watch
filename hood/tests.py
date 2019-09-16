from django.test import TestCase
from .models import Location,Business,Post,NeighbourHood,Occupant
from datetime import date as dt
from django.contrib.auth.models import User


#Location Test
class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        self.nrb=Location(locationName='Nairobi')

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nrb,Location))   

     #Testing save method
    def test_save_method(self):
        self.nrb.save_loc()
        locations=Location.objects.all()
        self.assertTrue(len(locations)>0)  

    #Testing save multiple
    def test_save_multiple_locations(self):
        self.nrb.save_loc()

        test_mbs=Location(locationName='Mombasa')
        test_mbs.save_loc()

        locations=Location.objects.all()
        self.assertEqual(len(locations),2)


    #Testiing delete method
    def test_delete_method(self):
        self.nrb.save_loc()

        test_mbs=Location(locationName='Mombasa')
        test_mbs.save_loc()

        test_mbs.delete_loc()
        locations=Location.objects.all()
        self.assertEqual(len(locations),1)

class PostTestClass(TestCase):

    def setUp(self):
        self.test_user=User(username='sunday',email='sunday@gmail.com')
        self.test_user.save()

        self.new_post=Post(title='Post 1',description='post 1 is the bomb',image='post1.png',author=self.test_user)

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))   

     #Testing save method
    def test_save_method(self):
        self.new_post.save_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)>0)  

    #Testing save multiple
    def test_save_multiple_locations(self):
        self.new_post.save_post()

        test_post=self.new_post=Post(title='Post 2',description='post 2 is the nuclear',image='post2.png',author=self.test_user)
        test_post.save_post()

        posts=Post.objects.all()
        self.assertEqual(len(posts),2)

    def test_find_post_by_id(self):
        self.new_post.save_post()

        test_post=Post(title='Post 2',description='post 2 is the nuclear',image='post2.png',author=self.test_user)
        test_post.save_post()

        found_post=Post.get_post_by_id(2)
        self.assertEqual(found_post.title,test_post.title)

    def delete_post(self):
            



