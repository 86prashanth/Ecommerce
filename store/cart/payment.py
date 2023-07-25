from django.shortcuts import render 
from django.contrib.auth.decorators import login_required
from store.models import *
from django.http import JsonResponse,HttpResponse

@login_required(login_url='/login/')
def razorpaycheck(request):
    cart=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cart:
        total_price=total_price+item.product.selling_price * item.product_qty
    return JsonResponse({'total_price':total_price})

# my ordersview
def myorders(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'checkout/myorder.html',context)
#Orderview(single product wise)
def orderview(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context={'order':order,'orderitems':orderitems}
    return render(request,'checkout/orderview.html',context)