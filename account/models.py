from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Slot(models.Model):
    action = ('True', 'True'), ('False', 'False')
    car_id = models.CharField(max_length=20, null=True)
    vacant = models.CharField(max_length=10, choices=action, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
