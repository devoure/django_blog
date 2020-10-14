from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    likes_cheese = models.BooleanField(default=False)
    favourite_hamster_name = models.CharField(max_length = 50)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

