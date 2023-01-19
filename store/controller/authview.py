from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import Customuserform
from django.contrib.auth import authenticate,login,logout
def register(request):
    if request.method=='POST':
        form=Customuserform(request.POST)
        if form.is_valid():
            form.save()
            form=Customuserform()
            messages.success(request,'registered successfully login to continue')
            return redirect('login')
    else:
        form=Customuserform()
    return render(request,'auth/register.html',{'form':form})

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'you are already logged in')
        return redirect('/')
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            pswd=request.POST.get('password')
            user=authenticate(request,username=name,password=pswd)
            if user is not None:
                login(request,user)
                messages.success(request,'logged in successfully')
                return redirect('/')
            else:
                messages.error(request,'invalid username or password')
                return redirect('/login')
    return render(request,'auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'logged out successfully')
    return redirect('/')
    