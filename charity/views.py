from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import login, logout
from .forms import *
from django.contrib import messages


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

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            messages.error(request, 'Wprowadź dane')
            return redirect('login')

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Błędny e-mail lub hasło')
        return redirect('login')


class Register(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not (name and surname and email and password):
            messages.error(request, 'Wprowadź dane')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Hasła muszą być takie same. Spróbuj ponownie')
            return redirect('register')

        user = User.objects.create_user(first_name=name, last_name=surname, password=password, email=email,
                                        username=email, is_active=True)
        login(request, user)
        return redirect('index')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('index')
