from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    message = models.CharField(max_length=1000, blank=True)
    time = models.DateTimeField(blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    sender = models.PositiveIntegerField(blank=True)
    room_name = models.CharField(blank=True, max_length=100)


    def save(self, *args, **kwargs):
        self.room_name = f'{self.receiver.id}and{self.sender}'
        

        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.sender} message'
    
