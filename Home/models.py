from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Properties(models.Model):
    options = (("Apartment","Apartment"),("House","House"),("office","office"),("Villa","Villa"))

    Name = models.CharField(max_length=255)
    category = models.CharField(max_length= 50,choices = options, default = "House" )
    Squre_Feet = models.FloatField(null=True,blank=True)
    Bed_Rooms = models.IntegerField(null=True,blank=True)
    Bath_Rooms = models.IntegerField(null=True,blank=True)
    Place = models.CharField(max_length=255)
    Date = models.DateField(auto_now_add=True)
    District = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Rent_per_month = models.FloatField()
    Description = models.CharField(max_length=1000)
    Image = models.FileField(upload_to="Property_image")
    Status = models.BooleanField(default=True)
    User_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

class Contract(models.Model):
    Tenent = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    Landlord = models.CharField(max_length=11, null=True, blank=True)
    properties = models.ForeignKey(Properties, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True) 
    approvel = models.BooleanField(default=False)

