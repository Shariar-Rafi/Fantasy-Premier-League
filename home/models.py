from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#makemigrations means- create changes and store in a file
#migrate means- apply the pending changes created by makemigrations

class Contact(models.Model): #model_table_creation
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateField()   
    def __str__(self):
        return self.name     #for returning names on admin panel of the post publishers

# Create your models here.
# UserProfile (id, phone_number, profile_picture, address,  user_id)

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Player(models.Model):
    game_type = models.CharField(max_length=20)
    player_type = models.CharField(max_length=20)
    team_name = models.CharField(max_length=50)
    User_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
