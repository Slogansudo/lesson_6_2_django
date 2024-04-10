
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password


def home_page1(request):
    return render(request, 'home_view.html')


"""def register_view(request):
    return render(request, 'register_view.html')


def login_view(request):
    return render(request, 'login_view.html')

"""


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'auth/register_user.html', {'form': form})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register_view')
        else:
            user = User.objects.filter(username=username)
            if user:
                return redirect('register_view')
            else:
                password = make_password(password1)
                user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                user.save()
                return redirect('home_page1')


class UsersLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'auth/login_users.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        #user = User.objects.filter(username=username, password=password)
        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home_page1')
        else:
            return render(request, 'login_not_found.html')


class UsersLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home_page1')
