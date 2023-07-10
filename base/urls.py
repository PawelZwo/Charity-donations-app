from django.contrib import admin
from django.urls import path
from charity.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', LandingPage.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('add-donation/', AddDonation.as_view(), name='add_donation'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<pk>/', Profile.as_view(), name='profile'),
]
