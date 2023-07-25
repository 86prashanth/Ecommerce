from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from store.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app/index.html')

# collection view 
def collections(request):
    category=Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'collections/collection.html',context)

#  category wise product view
def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={"products":products,'category':category}
        return render(request,'collections/products/index.html',context)
    else:
        messages.warning(request,'no such category found..')
        return redirect('collections/')
    

# product detail view
def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            products=Product.objects.filter(slug=prod_slug,status=0).first
            context={'products':products}
        else:
            messages.error(request,'no such product found')
            return redirect('collections')
    else:
        messages.error(request,"no such category found")
        return redirect('collections')
    return render(request,'collections/products/product_view.html',context)


# productlist view 
def productlistAjax(request):
    products=Product.objects.filter(status=0).values_list('name', flat=True)
    productslist=list(products)
    
    return JsonResponse(productslist, safe=False)

# # search
# def searchproduct(request):
#     blogs = Product.objects.all()
#     if request.method == 'POST':
#         search = request.GET.get('productsearch', '')
#         blogs = Product.objects.filter(name__contains=search).first()
#         return render(request, 'app/search_product.html', context={'search':search, 'blogs':blogs})
def searchproduct(request):
    if request.method=="POST":
        searchedterm=request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product=Product.objects.filter(name__icontains=searchedterm).first()
            if product:
                return render(request, 'app/search_product.html', context={'search':product})
                # return redirect('collections/' +product.category.slug+ '/'+product.slug)
                # return redirect('collections')
            else:
                messages.info(request,"No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
            
    return redirect(request.META.get('HTTP_REFERER'))