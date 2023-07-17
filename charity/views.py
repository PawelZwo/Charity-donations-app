from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import login, logout
from .forms import *
from django.contrib import messages
from random import sample


class LandingPage(View):
    def get(self, request):
        organisations = Institution.objects.filter(type='organizacja pozarządowa')
        foundations = Institution.objects.filter(type='fundacja')
        local_funding = Institution.objects.filter(type='zbiórka lokalna')
        context = {
            'bags': Donation.objects.aggregate(sum_bags_quantity=Sum('quantity')),
            'places': Institution.objects.all().count(),
        }

        if organisations.count() >= 5 and foundations.count() >= 5 and local_funding.count() >= 5:
            context_sampled = {
                                  'organisations': sample(list(organisations), 5),
                                  'fundations': sample(list(foundations), 5),
                                  'locals': sample(list(local_funding), 5)
                              } | context
            return render(request, 'index.html', context_sampled)
        else:
            context_not_sampled = {
                                      'organisations': organisations,
                                      'fundations': foundations,
                                      'locals': local_funding
                                  } | context
            return render(request, 'index.html', context_not_sampled)


class AddDonation(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'institutions': Institution.objects.all()
        }
        return render(request, 'form.html', context)

    def post(self, request):
        categories = request.POST.getlist('categories')
        quantity = request.POST.get('bags')
        institution = request.POST.get('organization')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        user = request.user.pk

        donation = Donation.objects.create(
            quantity=quantity, institution_id=institution, address=address, phone_number=phone_number,
            city=city, zip_code=zip_code, pick_up_date=pick_up_date, pick_up_time=pick_up_time,
            pick_up_comment=pick_up_comment, user_id=user
        )
        donation.categories.set(categories)
        donation.save()

        return redirect('donation_confirmation')


class DonationConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')


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
        user = User.objects.get(pk=pk)
        users_donations = Donation.objects.filter(user=pk)
        context = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'donations_all': users_donations.count,
                   'all_pending': users_donations.filter(is_taken=False).order_by('pick_up_date'),
                   'all_taken': users_donations.filter(is_taken=True).order_by('picked_up_on')
                   }
        return render(request, 'profile.html', context)

    def post(self, request, pk):
        taken_donation = Donation.objects.get(pk=request.POST.get('submit'))
        taken_donation.is_taken = True
        taken_donation.picked_up_on = date.today()
        taken_donation.save()
        return redirect('profile', pk=request.user.pk)


class PasswordConfirmation(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'password_confirmation.html')

    def post(self, request):
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password2')
        if request.user.check_password(password_confirmation) and password_confirmation == password:
            return redirect('password_change')
        else:
            messages.error(request, 'Hasła są różne od siebie lub nie są zgodne z Twoim obecnym hasłem.')
            return render(request, 'password_confirmation.html')


class ChangePassword(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'password_change.html')

    def post(self, request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('password')
        new_password_confirmation = request.POST.get('password2')
        if request.user.check_password(old_password) and new_password_confirmation == new_password:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Hasło poprawnie zmienionne.')
            login(request, request.user)
            return redirect('profile', pk=request.user.pk)
        else:
            messages.error(request, 'Obecne hasło jest nieprawidłowe i/lub nie wprowadziłxś takich sam haseł.')
            return render(request, 'password_change.html')
