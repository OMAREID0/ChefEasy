from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = "images/", null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    about = models.TextField(max_length=250, blank=True, null=False)

    def __str__(self):
        return str(self.user.username)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)