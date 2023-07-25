from django.shortcuts import redirect,render
from django.contrib import messages 
from store.models import Product,Cart,Wishlist,Profile
from django.contrib.auth.decorators import login_required

# checkout
@login_required(login_url='/login/')
def checkout_view(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.Quantity:# check models product and cart
            Cart.objects.delete(id=item.id)
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price=total_price + item.product.selling_price * item.product_qty

    userprofile=Profile.objects.filter(user=request.user).first()
    context={'cartitems':cartitems,'total_price':total_price,'userprofile':userprofile}
    return render(request,'checkout/checkout.html',context)