from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput, ModelForm
from .models import Properties



class UserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username','email','password1','password2']
        
        widgets = {
            "first_name":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"First Name"}),
            "username":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"Username"}), 
            "email":TextInput(attrs={"class":"form-control border-0 py-3","placeholder":"Email Id"}),    
        }  
        
    def __init__(self, *args, **kwargs):
        super(UserAddForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control border-0 py-3', 'placeholder': 'Password confirmation'})

class PropertyAddForm(ModelForm):
    class Meta:
        model = Properties
        fields = ["Name","Squre_Feet","Bed_Rooms","Bath_Rooms","Rent_per_month","Place","District","State","Description","Image"] 