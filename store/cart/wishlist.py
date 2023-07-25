from django.shortcuts import redirect,render
from django.contrib import messages 
from django.http import JsonResponse
from store.models import Product,Cart,Wishlist
from django.contrib.auth.decorators import login_required

# wishlistview
@login_required(login_url='/login/')
def wishlistview(request):
    wishitems=Wishlist.objects.filter(user=request.user)
    context={'wishitems':wishitems}
    return render(request,'wishlist/wishlistview.html',context)

# addtowishlist
def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({"status":'Product already is wishlist'})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'Product Added To wishlist'})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to Continue'})
    return redirect('home')

# delete wishlistitem
def deletewishlistitem(request):
    if request.method== 'POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem=Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product Removed from wishlist"})
            else:
                return JsonResponse({'status':'Product not found in wishlist'})
        else:
            return JsonResponse({'status':'login to continue'})
            
    return redirect('home')