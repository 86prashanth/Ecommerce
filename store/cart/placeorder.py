from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.contrib import messages 
from store.models import Product,Cart,Wishlist,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
# checkout
@login_required(login_url='/login/')
def placeorder(request):
    if request.method=='POST':
        currentuser=User.objects.filter(id=request.user.id).first()
        # if user is first time it filling the collomns
        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname') # check in database in 
            currentuser.last_name=request.POST.get('lname') 
            currentuser.save()

        # profile check 
        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')
            userprofile.save()

        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.Address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')
        neworder.payment_mode=request.POST.get('payment_mode')
        neworder.payment_id=request.POST.get('payment_id')
        cart=Cart.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price + item.product.selling_price * item.product_qty
        neworder.total_price=cart_total_price
        trackno='prashanth'+str(random.randint(111111,999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno='prashanth' +str(random.randint(111111,999999))
        neworder.tracking_no=trackno
        neworder.save()
        neworderitems=Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )
            # to decreate the product quqnatity from avaialble stock
            orderproduct=Product.objects.filter(id=item.product_id).first()
            orderproduct.Quantity=orderproduct.Quantity-item.product_qty
            orderproduct.save()        
        # To clear user'cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request,'your order has been successfully')
        paymode=request.POST.get('payment_mode')
        if (paymode=="Paid by Razorpay" or paymode == "Paid by PayPal"):
            return JsonResponse({'status':"Your order has been successfully"})
    return redirect('home')