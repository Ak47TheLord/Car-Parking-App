from django.db import models


# Create your models here.
class Slot(models.Model):
    car_id = models.CharField(max_length=20)
    vacant = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )

    def __str__(self):
        return f'{self.car_id})'
