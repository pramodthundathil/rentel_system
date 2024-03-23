from django.shortcuts import render, redirect
from .forms import UserAddForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import admin_only
from django.contrib.auth.models import User, Group
from .forms import PropertyAddForm, PropertySaleAddForm
from .models import Properties, Contract, PropertiesSale, StaffProfile, SaleCart, Sale
from django.contrib.auth.decorators import login_required


# Create your views here.
@admin_only
def HomePage(request):
    properties = Properties.objects.all()[::-1]
    properties1 = PropertiesSale.objects.all()[::-1]
    context = {"properties":properties,"properties1":properties1}
    return render(request,"index.html",context)


@login_required(login_url="SignIn")
def AdminIndex(request):
    form = UserAddForm()
    staff = StaffProfile.objects.all()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='staff')
            user.groups.add(group) 
            user.save()
            staff = StaffProfile.objects.create(user = user , staffId = user.id,tenentId = request.user.id )
            staff.save()
            messages.success(request,"Staff Registration Successfull")
            return redirect("AdminIndex")
        else:
            messages.error(request,"Something went Wrong!!! Try To use passwprd Includes (UPPERCASE, Numbers, Sepecial Characters and Minimum Legth 8  Characters) or User or email id Already Exists")
            return redirect("AdminIndex")
    conetxt = {
        "form":form,
        "staff":staff
    }
    return render(request,"adminindex.html",conetxt)

def deletestaff(request,pk):
    staff = StaffProfile.objects.get(id = pk)
    staff.user.delete()
    staff.delete()
    messages.success(request,"Staff deleted Successfull")
    return redirect("AdminIndex")



@login_required(login_url="SignIn")
def LandLoardIndex(request):
    return render(request,"landloardindex.html")


def StaffIndex(request):
    cart  = SaleCart.objects.filter(staff__user = request.user)

    context  = {
        "cart":cart
    }
    return render(request,"staffindex.html",context)

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
            formdata.Status = True
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
    cart = SaleCart.objects.filter(property__User_id = request.user )
    bookigs = Contract.objects.filter(Landlord = str(request.user.id), approvel = False)
    staffs = StaffProfile.objects.all()
    context = {
        "bookings":bookigs,
        "cart":cart,
        "staffs":staffs
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
    booking = Contract.objects.filter(properties = propertys, approvel = False ).delete()
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

def Agreement1(request,pk):
    pr = Properties.objects.get(id = pk)
    return render(request,"rentagreement1.html",{"pr":pr})



def PropertiesforSale(request):
    properties = PropertiesSale.objects.all()[::-1]
    context = {"properties":properties}
    return render(request,"allpropertiesforsale.html",context)


def LandloadSaleProperties(request):
    form = PropertySaleAddForm()
    properties = PropertiesSale.objects.filter(User_id = request.user)[::-1] 
    if request.method == "POST":
        form = PropertySaleAddForm(request.POST,request.FILES)
        if form.is_valid:
            formdata = form.save()
            formdata.User_id = request.user 
            formdata.Status = True
            formdata.save()
            messages.info(request,"Property added to List")
            return redirect("LandloadSaleProperties")
        else:
            messages.info(request,"Data Not Saved")
        

    context = {
        "form":form,
        "properties":properties
    }
    return render(request,"propertyforsale.html",context)


@login_required(login_url="SignIn")
def PropertySaleSingleView(request,pk):

    prop = PropertiesSale.objects.get(id = pk)
    context = {
        "prop":prop
    }
    return render(request, "salesingleview.html",context)

@login_required(login_url="SignIn")
def BookForBuy(request,pk):
    prop = PropertiesSale.objects.get(id = pk)

    if SaleCart.objects.filter(Tenent = request.user,property = prop).exists():
        messages.info(request,"You alreday Have a Booking On this property.....")
    else:
        cart = SaleCart.objects.create(Tenent  = request.user,property = prop,staff_comment = "Staff Not Assigned"  )
        cart.save()
        messages.info(request,"Interest on property is sent.....")
    return redirect("PropertySaleSingleView",pk=pk)


def MybookingSale(request):
    
    cart = SaleCart.objects.filter(Tenent = request.user)

    context = {
        "cart":cart
    }
    return render(request,"mybookingsale.html",context)

def DeleteSaleBook(request,pk):
    SaleCart.objects.get(id = pk).delete()
    messages.info(request,"Item deleted.....")
    return redirect("MybookingSale")

def AssignStaff(request,pk):
    Cart = SaleCart.objects.get(id = pk)
    if request.method == "POST":
        staff_id = request.POST["staff"]
        staff = StaffProfile.objects.get(id = int(staff_id))
        Cart.staff = staff
        Cart.staff_comment = "Staff assigned"
        Cart.save()
        messages.info(request, "Staff addedd......")
        return redirect("LandlordBooking")
    return redirect("LandlordBooking")


def AddStaffComment(request,pk):
    cart = SaleCart.objects.get(id = pk)
    if request.method == "POST":
        comment = request.POST['clr']
        cart.staff_comment = comment
        cart.staff_clearence = comment
        if comment == "Document Verified":
            cart.staff_clear_status = True
        cart.save()
        messages.info(request,"comment added...")
        return redirect("StaffIndex")
    return redirect("StaffIndex")

def Approvesale(request,pk):
    cart = SaleCart.objects.get(id = pk)
    sale = Sale.objects.create(Owner = cart.Tenent,property = cart.property,Old_owner = cart.property.User_id.id  )
    sale.save()
    sale.property.Status = False
    sale.save()
    cart.delete()
    messages.info(request,"Sale Compleated........")
    return redirect("Saledproperty")


def Saledproperty(request):
    sale = Sale.objects.filter(property__User_id = request.user)
    context = {
        "sale":sale
    }
    return render(request,"saledproperty.html",context)

def DeletesalebookingLandlord(request,pk):
    SaleCart.objects.get(id = pk).delete()
    messages.info(request,"Sale Compleated........")
    return redirect("LandlordBooking")

def OwnedProperties(request):
    sale = Sale.objects.filter(Owner = request.user)
    return render(request,"ownedproperties.html",{"sale":sale})


