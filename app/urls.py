from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',homepage,name='home'),
    path('login',loginpage,name='login'),
    path('register',registerpage,name='register'),
    path('logout',logoutpage,name='logout'),
    path('shop',shoppage,name="shop"),
    path('addpro',addproduct,name = 'addpro'),
    path('editpro/<int:pid>',editproduct,name = 'editpro'),
    path('deletepro/<int:pid>',deleteproduct,name = 'deletepro'),
    path('prodetails/<int:pid>',prodetails,name='prodetails'),
    path('addcat',addcat,name="addcat"),
    path('addcart/<int:pid>',addcart,name='addcart'),
    path('cart',viewcart,name='cart'),
    path('remove/<int:pid>',remove,name='remove')
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)