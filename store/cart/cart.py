from django.shortcuts import redirect,render
from django.contrib import messages 
from django.http import JsonResponse
from store.models import Product,Cart
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({"status":'Product Already in Cart'})
                else:
                    prod_qty=int(request.POST.get('product_qty'))

                    if product_check.Quantity>=prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':'Prdouct added Successfully'})
                    else:
                        return JsonResponse({'status':"Only"+str(product_check.Quantity)+"quantiy available"})
            else:
                return JsonResponse({'status':'No Such Product found'})
        else:
            return JsonResponse({'status':'Login into Continue'})
    return redirect('home')


# cartview
@login_required(login_url='login')
def cartview(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'cart/cartview.html',context)


#updatecart
def updatecart(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':'updated Successfully'})
    return redirect('home')


# delete cartitem

def deletecartitem(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem=Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status':"deleted SuccessFully"})
    return redirect('home')

