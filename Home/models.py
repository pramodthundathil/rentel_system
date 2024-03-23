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

    def __str__(self):
        return str(self.Name)

class PropertiesSale(models.Model):
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
    amount = models.FloatField()
    Description = models.CharField(max_length=1000)
    Image = models.FileField(upload_to="Property_image")
    Status = models.BooleanField(default=True)
    User_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return str(self.Name)

class Contract(models.Model):
    Tenent = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    Landlord = models.CharField(max_length=11, null=True, blank=True)
    properties = models.ForeignKey(Properties, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True) 
    approvel = models.BooleanField(default=False)

    def __str__(self):
        return str("contract with ") + str(self.Tenent) + " on property " + str(self.properties) 
    

class StaffProfile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    staffId = models.PositiveBigIntegerField()
    tenentId = models.PositiveBigIntegerField()

class SaleCart(models.Model):
    options = (("pending","pending"),("Rejected","Rejected"),("Document Cleared","Document Cleared"))
    property = models.ForeignKey(PropertiesSale,on_delete = models.CASCADE)
    Tenent = models.ForeignKey(User,on_delete = models.CASCADE, null=True, blank=True )
    date = models.DateField(auto_now_add = True)
    staff = models.ForeignKey(StaffProfile,on_delete = models.SET_NULL,null = True)
    staff_comment = models.CharField(max_length = 1000)
    staff_clearence = models.CharField(default = "pending",max_length = 100, choices = options )
    staff_clear_status = models.BooleanField(default = False)

    def __str__(self):
        return str("Cart with ") + str(self.Tenent) + " on property " + str(self.property) 

class Sale(models.Model):
    Owner =  models.ForeignKey(User,on_delete = models.CASCADE, null=True, blank=True )
    Old_owner = models.CharField(max_length = 11)
    sale_date = models.DateField(auto_now_add = True)
    property =  models.ForeignKey(PropertiesSale,on_delete = models.CASCADE) 

    def __str__(self):
        return str("Sale with ") + str(self.Owner) + " on property " + str(self.property) 
    

