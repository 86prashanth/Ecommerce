from django.shortcuts import redirect,render 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from store.forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Register 
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully! Login to continue')
            return redirect('login')
    context={'form':form}
    return render(request,'auth/register.html',context)

# loginpage
def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'your already logged in')
        return redirect('home')
    else:
    # first you have to check this code whether is login or not
        if request.method=='POST':
            name=request.POST.get("username")
            pswd=request.POST.get("password")
            user=authenticate(request,username=name,password=pswd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect('home')
            else:
                messages.error(request,'invalid Username or Password')
                return redirect('login')
        
        return render(request,'auth/login.html')
# changepassword
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
        return redirect('home')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'auth/change_password.html',{'form':form})
# logout page

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged Out Successfully")
        return redirect('home')
