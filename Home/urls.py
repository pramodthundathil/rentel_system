from django.urls import path 
from .import views

urlpatterns = [
    path("",views.HomePage,name="HomePage"),
    path("LandLoardIndex",views.LandLoardIndex,name="LandLoardIndex"),    
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),    
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("UserTypeConfirmation",views.UserTypeConfirmation,name="UserTypeConfirmation"),
    path("LandLoadConfirm",views.LandLoadConfirm,name="LandLoadConfirm"),
    path("TenentConfirm",views.TenentConfirm,name="TenentConfirm"),
    path("Propertyadd",views.Propertyadd,name="Propertyadd"),
    path("PropertySingleView/<int:pk>",views.PropertySingleView,name="PropertySingleView"),
    path("PropertySaleSingleView/<int:pk>",views.PropertySaleSingleView,name="PropertySaleSingleView"),
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
    path("Agreement1/<str:pk>",views.Agreement1,name="Agreement1"),
    path("PropertiesforSale",views.PropertiesforSale,name="PropertiesforSale"),
    path("LandloadSaleProperties",views.LandloadSaleProperties,name="LandloadSaleProperties"),
    path("deletestaff/<int:pk>",views.deletestaff,name="deletestaff"),
    path("StaffIndex",views.StaffIndex,name="StaffIndex"),
    path("BookForBuy/<int:pk>",views.BookForBuy,name="BookForBuy"),
    path("MybookingSale",views.MybookingSale,name="MybookingSale"),
    path("DeleteSaleBook/<int:pk>",views.DeleteSaleBook,name="DeleteSaleBook"),
    path("AssignStaff/<int:pk>",views.AssignStaff,name="AssignStaff"),
    path("AddStaffComment/<int:pk>",views.AddStaffComment,name="AddStaffComment"),
    path("Saledproperty",views.Saledproperty,name="Saledproperty"),
    path("Approvesale/<int:pk>",views.Approvesale,name="Approvesale"),
    path("DeletesalebookingLandlord/<int:pk>",views.DeletesalebookingLandlord,name="DeletesalebookingLandlord"),
    path("OwnedProperties",views.OwnedProperties,name="OwnedProperties"),




]
