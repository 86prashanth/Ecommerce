from django.contrib import messages
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from store.models import *

@login_required(login_url='login')
def add_wishlist(request):
    wishlist_items=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist_items}
    return render(request,'products/wishlist.html',context)


def add_to_wishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({'status':'product is already wishlist'})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'product added to wishlist'})
            else:
                return JsonResponse({'status':'No such product found'})   

        else:
            return JsonResponse({'status':'login to continue'})
    return redirect('/')

def delete_to_wishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                Wishlistitem=Wishlist.objects.get(product_id=prod_id)
                Wishlistitem.delete()
                return JsonResponse({'status':'product removed from wishlist'})
            else:
                return JsonResponse({'status':'product not found in wishlist'})
        else:
            return JsonResponse({'status':'deleted sucessfully'})
    return redirect('/')

    