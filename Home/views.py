from django.shortcuts import render, redirect
from .forms import UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import admin_only
from django.contrib.auth.models import User, Group
from .forms import PropertyAddForm
from .models import Properties, Contract
from django.contrib.auth.decorators import login_required


# Create your views here.
@admin_only
def HomePage(request):
    properties = Properties.objects.all()[::-1]
    context = {"properties":properties}
    return render(request,"index.html",context)
@login_required(login_url="SignIn")
def LandLoardIndex(request):
    return render(request,"landloardindex.html")

def SignIn(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST["pswd"]
        user = authenticate(request,username= uname, password = password)
        if user is not None:
            login(request,user)
            return redirect('HomePage')
        else:
            messages.info(request,"Username or Password Incorrect")
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()

    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect("SignIn")

        else:
            messages.error(request,"Something went Wrong!!! Try To use passwprd Includes (UPPERCASE, Numbers, Sepecial Characters and Minimum Legth 8  Characters) or User or email id Already Exists")
            return redirect("SignUp")
    
    context = {"form":form}
    return render(request,"register.html",context)

def UserTypeConfirmation(request):
    return render(request,"usertypeconformation.html")

def LandLoadConfirm(request):
    user = request.user 
    group = Group.objects.get(name="landloard")
    user.groups.add(group)
    user.save()
    return redirect('HomePage')

def TenentConfirm(request):
    user = request.user 
    group = Group.objects.get(name="tenent")
    user.groups.add(group)
    user.save()
    return redirect('HomePage')

def SignOut(request):
    logout(request)
    return redirect('SignIn')


# Property Handling

@login_required(login_url="SignIn")
def Propertyadd(request):
    form = PropertyAddForm()
    propertys = Properties.objects.filter(User_id = request.user)[::-1] 

    if request.method == "POST":
        form = PropertyAddForm(request.POST,request.FILES)
        if form.is_valid:
            formdata = form.save()
            formdata.User_id = request.user 
            formdata.status = True
            formdata.save()
            messages.info(request,"Property added to List")
            return redirect("Propertyadd")
        else:
            messages.info(request,"Data Not Saved")
        
        return redirect("Propertyadd")

    context = {"form":form,"propertys":propertys}
    return render(request,"properties.html",context)

@login_required(login_url="SignIn")
def PropertySingleView(request,pk):

    prop = Properties.objects.get(id = pk)
    context = {
        "prop":prop
    }
    return render(request, "rentsingleview.html",context)

@login_required(login_url="SignIn")
def BookRentelProperty(request,pk):

    prop = Properties.objects.get(id = pk)
    contract = Contract.objects.create(Tenent = request.user, Landlord = prop.User_id.id, properties = prop)
    contract.save()
    messages.info(request,"Property Booked Wait For Aproval....")
    return redirect("PropertySingleView",pk)

def TenentBookings(request):

    contract = Contract.objects.filter(Tenent = request.user)
    context = {
        "contract":contract
    }
    return render(request,"mybookings.html",context)

def DeleteTenentBooking(request,pk):
    booking  = Contract.objects.get(id = pk).delete()
    messages.info(request, "Booking Deleted")
    return redirect("TenentBookings")

def AllPropertiesTenent(request):
    properties = Properties.objects.all()[::-1]
    context = {"properties":properties}
    return render(request,"allpropertiestenent.html",context)

def LandlordBooking(request):

    bookigs = Contract.objects.filter(Landlord = str(request.user.id), approvel = False)
    context = {
        "bookings":bookigs
    }
    return render(request,"landloadbookings.html",context)

def contracts(request):

    bookings = Contract.objects.filter(Landlord = str(request.user.id), approvel = True)
    context = {
        "bookings":bookings
    }
    return render(request, "contracts.html",context)
        
def ApproveContracts(request,pk):
    booking = Contract.objects.get(id = pk)
    booking.approvel = True
    booking.save()
    propertys = booking.properties
    propertys.Status = False
    propertys.save()

    messages.info(request, "Booking Approved!!!!!")

    return redirect("contracts")

def DeleteTenentBookingLandlord(request,pk):
    booking  = Contract.objects.get(id = pk).delete()
    messages.info(request, "Booking Deleted")
    return redirect("LandlordBooking")

def ViewTenentDetails(request,pk):
    user = User.objects.get(id = pk)
    context = {
        "user":user
    }
    return render(request,"tenentdetails.html",context)

def LandLordInformation(request,pk):
    user = User.objects.get(id = int(pk))
    context = {
        "user":user
    }
    return render(request, "landloarsinformation.html",context)


def Agreement(request,pk):
    pr = Properties.objects.get(id = pk)
    return render(request,"rentagreement.html",{"pr":pr})