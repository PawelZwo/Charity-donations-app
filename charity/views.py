from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import login, logout, update_session_auth_hash
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm


class LandingPage(View):
    def get(self, request):
        context = {
            'bags': Donation.objects.all().count(),
            'places': Institution.objects.all().count(),
            'organisations': Institution.objects.filter(type='organizacja pozarządowa'),
            'fundations': Institution.objects.filter(type='fundacja'),
            'locals': Institution.objects.filter(type='zbiórka lokalna')
        }
        return render(request, 'index.html', context)


class AddDonation(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'institutions': Institution.objects.all()
        }
        return render(request, 'form.html', context)


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
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            messages.error(request, 'Błędny e-mail lub hasło')
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
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
            messages.error(request, 'Hasła muszą być takie same, spróbuj ponownie')
            return redirect('register')

        user = User.objects.create_user(first_name=name, last_name=surname, password=password, email=email,
                                        username=email, is_active=True)
        login(request, user)
        return redirect('index')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class Profile(LoginRequiredMixin, View):

    def get(self, request, pk):
        context = {'first_name': User.objects.get(pk=pk).first_name,
                   'last_name': User.objects.get(pk=pk).last_name,
                   'email': User.objects.get(pk=pk).email
                   }
        return render(request, 'profile.html', {'profile': context})


class PasswordConfirmation(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'password_confirmation.html')

    def post(self, request):
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password2')
        if request.user.check_password(password_confirmation):
            return redirect('password_change')
        else:
            messages.error(request, 'Hasła są różne od siebie lub nie są zgodne z Twoim obecnym hasłem.')
            return render(request, 'password_confirmation.html')


class ChangePassword(LoginRequiredMixin, View):

    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'password_change.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Pomyślnie zmieniono hasło!')
            return redirect('profile')
        else:
            messages.error(request, 'Wprowadź poprawnie nowe hasło.')
