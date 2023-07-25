from django.urls import path 
from .views import *
from store.cart import cart,wishlist,checkout,placeorder,payment
from store.controller import auth_view


urlpatterns=[
    path('',index,name='home'),
    path('collections/',collections,name='collections'),
    path('collections/<str:slug>',collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>/',productview,name='productview'),
    path('product-list/',productlistAjax,name='product-list'),
    path('searchproduct/',searchproduct,name='searchproduct'),
    path('register/',auth_view.register,name='register'),
    path('login/',auth_view.loginpage,name='login'),
    path('changepassword/',auth_view.change_password,name='changepassword'),
    path('logout/',auth_view.logoutpage,name='logout'),
    path('add-to-cart/',cart.addtocart,name='add-to-cart'),
    path('cartview/',cart.cartview,name='cartview'),
    path('updatecart/',cart.updatecart,name='updatecart'),
    path('deletecartitem/',cart.deletecartitem,name='deletecartitem'),
    path('wishlistview/',wishlist.wishlistview,name='wishlistview'),
    path('add-to-wishlist/',wishlist.addtowishlist,name='add-to-wishlist'),
    path('deletewishlistitem/',wishlist.deletewishlistitem,name='deletewishlistitem'),
    path('checkout/',checkout.checkout_view,name='checkout'),
    path('place-order/',placeorder.placeorder,name='place-order'),
    path('proceed-to-pay/',payment.razorpaycheck,name='proceed-to-pay'),
    path('my-order/',payment.myorders,name='my-order'),
    path('orderview/<str:t_no>',payment.orderview,name='orderview'),
]
