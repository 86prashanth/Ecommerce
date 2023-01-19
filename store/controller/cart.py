from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from store.models import Product,Cart
from django.contrib.auth.decorators import login_required


def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_chcek=Product.objects.get(id=prod_id)
            if(product_chcek):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                  return JsonResponse({'status':'product already in cart'}) 
                else:
                    product_qty=int(request.POST.get('product_qty'))
                    if product_chcek.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=product_qty)
                        return JsonResponse({'status':'product added succefully'})
                    else:
                        return JsonResponse({'status':"only "+str(product_chcek.quantity)+" qunatity avaialable "})
            else:
                return JsonResponse({'status':'No such record found'})
        else:
            return JsonResponse({'status':'login to continue'})
    return redirect('/')

@login_required(login_url='login')
def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'products/cart.html',context)

def updatecart(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':'updated Successfully'})
    return redirect('/')

def deletecartitem(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem=Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':'deleted sucessfully'})
    return redirect('/')
    