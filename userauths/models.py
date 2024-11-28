from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=16)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    otp = models.CharField(max_length=10,null=True,blank=True)
    refresh_token = models.CharField(max_length=255,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    # def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
    #     return super().save(force_insert, force_update, using, update_fields)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="user_folder", default='avatar.jpg',blank=True, null=True)
    full_name = models.CharField(max_length=100)
    about = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    # def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
    #     return super().save(force_insert, force_update, using, update_fields)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)