#from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static  import static
from django.conf  import settings
#from django.contrib.auth import views as auth_views
from django.urls import path, include
from .models import ad

urlpatterns=[
    path('', views.index, name='index page'),
    path('signup', views.signup, name='Signup'),
    path('login/', views.login, name='Login'),
    path('logout', views .logout, name='Logout'),
    path('contact', views.contact, name='Contact'),
    path('adpost', views.adpost, name='Ad-Post'),
    path('products', views.products, name='Products'),
    path('changepass', views.changepassword, name='Change Password'),
    path('logout', views.logout, name='Log out'),
    path('categories',views.categories, name='Category'),
    path('singlead/<int:ad_id>/', views.singlead, name='Single-ad'),
    path('sendmessage/<int:ad_id>/', views.sendmessage, name='sendmessage'),
    path('productscat/<int:id>/', views.productscat,name='Products-cat'),
    path('about', views.about, name='About us'),
    path('search', views.search, name='Search'),
    path('chatbox/<int:id>/', views.chatbox, name='Chat Box'),
    path('mypostedad', views.mypostedad, name='ADs Posted'),
    path('deletedata/<int:id>', views.deletedata, name='Delete Data'),
    path('changedata/<int:id>', views.changedata, name='Change Data'),
    path('userprofile', views.userprofile, name='User-Profile'),

            ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)