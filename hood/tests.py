from django.test import TestCase

from django.test import TestCase
from .models import Bussiness, Neighbour, Profile
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):

 def setUp(self):
    self.user = User(username="", password="")
    self.user.save()
    self.neighbour= Neighbour(hood_name = "", hood_location= "", admin = self.user,hood_description='')
    self.neighbour.save()
    self.profile = Profile(bio='',email='', idNo='',user = self.user, neighbour = self.neighbour)

 def test_instance(self):
     self.assertTrue(isinstance(self.profile,Profile))

 def test_save_method(self):
    self.profile.save_profile()
    testsaved = Profile.objects.all()
    self.assertTrue(len(testsaved) > 0)

 def test_delete_method(self):
   self.profile.save_profile()
   testsaved = Profile.objects.all()
   self.assertTrue(len(testsaved) > 0)

class NeighbourTestClass(TestCase):
#Set up Method
  def setUp(self):
  
   self.user = User(username='')
   self.user.save()
   self.neighbour = Neighbour(hood_name='',hood_location='',hood_description="",hood_photo='photo.url',admin = self.user)
   self.neighbour.save_hood()

  def tearDown(self):
    Neighbour.objects.all().delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.neighbour,Neighbour))

  def test_create_neighbor(self):
    self.neighbour.save_hood()
    hoods = Neighbour.objects.all()
    self.assertTrue(len(hoods) > 0)

  def test_delete_neighbor(self):
   self.neighbour.save_hood()
   self.neighbour.delete_hood()
   hood = Neighbour.objects.all()
   self.assertTrue(len(hood) == 0)

class BusinessTestClass(TestCase):
    # Set up method

    def setUp(self):
        self.user = User(username="", password="")
        self.user.save()
        self.neighbour = Neighbour(
            hood_name="", hood_location="", admin=self.user, hood_description='')
        self.neighbour.save()
        self.business = Bussiness (business_email='',name='',neighbour_id ="")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Bussiness))

    def test_save_business(self):
        self.business.save_business()
        biz = Bussiness.objects.all()
        self.assertTrue(len(biz) > 0)
