from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userpage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    
    def __str__(self) -> None:
        return self.user.username