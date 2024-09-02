from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

class User(AbstractUser):
    user_permissions = models.ManyToManyField(Permission, related_name='user_set', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=False, default='Unknown')

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', verbose_name=('Image'))
    # name = models.CharField(max_length=255, blank=True, verbose_name=('Name'))
    # description = models.TextField(blank=True, verbose_name=('Description'))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=('Uploaded at'))

    def __str__(self):
        return self.image or f'Image {self.id}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_profile_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

