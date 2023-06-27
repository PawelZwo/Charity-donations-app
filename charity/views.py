from django.shortcuts import render
from django.views import View

from .models import *


class LandingPage(View):
    def get(self, request):
        context = {
            'bags': Donation.objects.all().count(),
            'organisations': Institution.objects.all().count()
        }
        return render(request, 'index.html', context)


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')
