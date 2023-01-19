from django.urls import path
from .views import *
from store.controller import authview,cart,wishlist,checkout,orders

urlpatterns = [
    path('',home,name='home'),
    path('collections/',collections,name='collections'),
    path('collections/<str:slug>',collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',productsview,name='productsview'),
    path('product-list',product_list,name='product_list'),
    path('searchproduct',searchproduct,name='searchproduct'),
    path('register/',authview.register,name='register'),
    path('login/',authview.loginpage,name='login'),
    path('logout/',authview.logoutpage,name='logout'),
    path('add-to-cart/',cart.addtocart,name='addtocart'),
    path('cart/',cart.viewcart,name='cart'),
    path('updatecart/',cart.updatecart,name='updatecart'),
    path('delete-cart-item/',cart.deletecartitem,name='deletecartitem'),
    path('wishlist/',wishlist.add_wishlist,name='wishlist'),
    path('addtowishlist/',wishlist.add_to_wishlist,name='addtowishlist'),
    path('deletewishlist/',wishlist.delete_to_wishlist,name='deletewishlist'),
    path('checkout/',checkout.checkout_view,name='checkout'),
    path('placeorder/',checkout.placeorder,name='placeorder'),
    path('process-to-pay/',checkout.razorpaycheck,name='process-to-pay'),
    path('myorders/',orders.myorders,name='myorders'),
    path('orderview/<str:t_no>/',orders.orderview,name='orderview'),
]
