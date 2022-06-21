from django.db import models
from django.contrib.auth.models import  User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Neighbour(models.Model):
    hood_name = models.CharField(max_length=200)
    hood_location = models.CharField(max_length=200)
    hood_description = models.TextField(max_length=500, blank=True)
    hood_photo = CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')


    def __str__(self):
        return self.hood_name
        # return f'{self.hood_name} neighbourhood'
    def save_hood(self):
        self.save()
    def delete_hood(self):
        self.delete()
    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)
    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name

#class profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNo = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    #profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    neighbour = models.ForeignKey(Neighbour, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    def update_profile(cls, id):
        Profile.objects.get(user_id=id)

#class Bussiness
class Bussiness(models.Model):
     business_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
     name = models.CharField(max_length=120)
     business_email = models.EmailField(max_length=254)
     neighbour_id = models.ForeignKey(Neighbour, on_delete=models.CASCADE, related_name='business')

     def __str__(self):
        return f'{self.name}Business'

     def save_business(self):
        self.save()

     def create_business(self):
            self.save()

     def delete_business(self):
        self.delete()

     @classmethod
     def find_business(cls,business_id):
        business = cls.objects.get(id = business_id)
        return business

     def update_business(self):
        name = self.name
        self.name = name
    
class Post(models.Model):
    
    category = models.CharField(max_length=120)
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    neighbour = models.ForeignKey(Neighbour, on_delete=models.CASCADE, related_name='neighbourhood_post')

    def __str__(self):
        return f'{self.title} Post'    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
