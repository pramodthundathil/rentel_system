from django.http import HttpResponse
from django.shortcuts import redirect


#decorator for user redirect...............
def unautenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('homescreen')
        else:
            return view_func(request,*args,**kwargs)
        
    return wrapper_func

# allowed user decorators................
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

#decorators for user wise redirect pages...............
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
            
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == None:
            return redirect("UserTypeConfirmation")

        if group == "admin":
            return redirect('AdminIndex')
            
        if group == 'tenent':
            return view_func(request, *args, **kwargs)
        
        if group == 'landloard':
            return redirect('LandLoardIndex')
        
        if group == 'officer':
            return redirect('LandLoardIndex')
        
        if group == 'staff':
            return redirect('StaffIndex')
        
              
    return wrapper_function