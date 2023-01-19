from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from store.models import Order,OrderItem


def myorders(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'orders/orders.html',context)

def orderview(request,t_no):
    orders=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems=OrderItem.objects.filter(order=orders)
    context={'orders':orders,'orderitems':orderitems}
    return render(request,'orders/view.html',context)

    


    