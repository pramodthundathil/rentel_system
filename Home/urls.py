from django.urls import path 
from .import views

urlpatterns = [
    path("",views.HomePage,name="HomePage"),
    path("LandLoardIndex",views.LandLoardIndex,name="LandLoardIndex"),    
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("UserTypeConfirmation",views.UserTypeConfirmation,name="UserTypeConfirmation"),
    path("LandLoadConfirm",views.LandLoadConfirm,name="LandLoadConfirm"),
    path("TenentConfirm",views.TenentConfirm,name="TenentConfirm"),
    path("Propertyadd",views.Propertyadd,name="Propertyadd"),
    path("PropertySingleView/<int:pk>",views.PropertySingleView,name="PropertySingleView"),
    path("BookRentelProperty/<int:pk>",views.BookRentelProperty,name="BookRentelProperty"),
    path("TenentBookings",views.TenentBookings,name="TenentBookings"),
    path("AllPropertiesTenent",views.AllPropertiesTenent,name="AllPropertiesTenent"),
    path("DeleteTenentBooking/<int:pk>",views.DeleteTenentBooking,name="DeleteTenentBooking"),
    path("LandlordBooking",views.LandlordBooking,name="LandlordBooking"),
    path("contracts",views.contracts,name="contracts"),
    path("ApproveContracts/<int:pk>",views.ApproveContracts,name="ApproveContracts"),
    path("DeleteTenentBookingLandlord/<int:pk>",views.DeleteTenentBookingLandlord,name="DeleteTenentBookingLandlord"),
    path("ViewTenentDetails/<int:pk>",views.ViewTenentDetails,name="ViewTenentDetails"),
    path("LandLordInformation/<str:pk>",views.LandLordInformation,name="LandLordInformation"),
    path("Agreement/<str:pk>",views.Agreement,name="Agreement"),



]
