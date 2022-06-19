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



# class NeighbourhoodTestClass(TestCase):
# #Set up Method
#   def setUp(self):
  
#    self.user = User(username='Amos')
#    self.user.save()
#    self.neighbourhood = Neighbourhood(hood_name='Rosya',hood_location='Nairobi',hood_description="hood of hoods",hood_photo='photo.url',admin = self.user)
#    self.neighbourhood.save_hood()


#   def tearDown(self):
#     Neighbourhood.objects.all().delete()

#   def test_instance(self):
#     self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

#   def test_create_neighborhood(self):
#     self.neighbourhood.save_hood()
#     hoods = Neighbourhood.objects.all()
#     self.assertTrue(len(hoods) > 0)

#   def test_delete_neighborhood(self):
#    self.neighbourhood.save_hood()
#    self.neighbourhood.delete_hood()
#    hood = Neighbourhood.objects.all()
#    self.assertTrue(len(hood) == 0)


# class BusinessTestClass(TestCase):
#     # Set up method

#     def setUp(self):

#         self.user = User(username="Amos", password="Amos24")
#         self.user.save()
#         self.neighbourhood = Neighbourhood(
#             hood_name="Roysa", hood_location="Nairobi", admin=self.user, hood_description='hood of hoods')
#         self.neighbourhood.save()
#         self.business = Bussiness (business_email='kipro@gmail.com',name='Avocado business',neighbourhood_id ="23")
    
#     def test_instance(self):
#         self.assertTrue(isinstance(self.business,Bussiness))

#     def test_save_business(self):
#         self.business.save_business()
#         biz = Bussiness.objects.all()
#         self.assertTrue(len(biz) > 0)
