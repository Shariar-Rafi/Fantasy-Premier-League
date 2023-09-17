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
    
class JTForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    TeamName = models.CharField(max_length=100)
    def __str__(self):
        return self.name 
    
class BF(models.Model):
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
   


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

class Coach(models.Model):
    c_id= models.IntegerField(primary_key=True) 
    team_name= models.CharField(max_length=100) 
    start_date_time= models.DateField() 
    coaching_duration= models.CharField(max_length=50)
    userprofile = models.ForeignKey(User, on_delete= models.CASCADE) 

class Team(models.Model):
    game_type = models.CharField(max_length=50)
    T_location = models.DateTimeField(max_length=50)
    team_name =  models.DateTimeField(max_length=50)
    C = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class GroundAdmin(models. Model):
    ga_id= models.IntegerField(primary_key=True)
    ground_name= models.CharField(max_length=100)
    userprofile = models.ForeignKey(User, on_delete= models.CASCADE) 

class Ground(models. Model):
    g_id= models.IntegerField(primary_key=True) 
    ground_name= models.CharField(max_length=100) 
    g_loaction= models.CharField(max_length=100)
    g_type= models.CharField(max_length=100) 
    g_admin = models.ForeignKey(GroundAdmin, on_delete= models.CASCADE)

class Booking(models. Model):
    b_id= models.IntegerField(primary_key=True) 
    match_date= models.DateTimeField(max_length=50) 
    match_time= models.DateTimeField(max_length=50)
    team= models.ForeignKey(Team, on_delete= models.CASCADE)
    Ground = models.ForeignKey(Ground, on_delete= models.CASCADE)

class C_payment(models. Model):
    id= models.IntegerField(primary_key=True) 
    payment_date= models.DateTimeField(max_length=50) 
    team= models.ForeignKey(Team, on_delete= models.CASCADE)
    amount= models.FloatField()
    coach= models.ForeignKey(Coach, on_delete= models.CASCADE)

class G_payment(models. Model):
    id= models.IntegerField(primary_key=True) 
    payment_date= models.DateTimeField(max_length=50) 
    team= models.ForeignKey(Team, on_delete= models.CASCADE)
    amount= models.FloatField()
    GA= models.ForeignKey(GroundAdmin, on_delete= models.CASCADE)




