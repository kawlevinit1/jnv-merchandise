from django.contrib import admin
from django.urls import path
from . import views
from .views.home import Index , store ,home
from .views.home import about ,contact
from .views.signup import signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.login import logout
from .views.login import Login
urlpatterns = [
    
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('about',about,name='about'),
    path('home',home,name='home'),
    path('contact',contact,name='contact'),
    path('signup', signup, name='signup'),
    path('logout', logout , name='logout'),
    path('login',Login.as_view() ,name='login'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
