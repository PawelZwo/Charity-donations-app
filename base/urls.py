from django.contrib import admin
from django.urls import path
from charity.views import *

urlpatterns = [
    path('', LandingPage.as_view(), name='index'),
    path('add-donation/', AddDonation.as_view(), name='add_donation'),
    path('donation-confirmation/', DonationConfirmation.as_view(), name='donation_confirmation'),

]

account_urls = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/<pk>/', Profile.as_view(), name='profile'),
    path('confirm-password/', PasswordConfirmation.as_view(), name='password_confirmation'),
    path('change-password/', ChangePassword.as_view(), name='password_change')
]

urlpatterns += account_urls
