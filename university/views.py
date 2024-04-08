
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.models import User
from .forms import UserLoginForm


def home_page1(request):
    return render(request, 'home_view.html')


def register_view(request):
    return render(request, 'register_view.html')


def login_view(request):
    return render(request, 'login_view.html')


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register_user.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            return redirect('register_users')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
            user.set_password(password1)
            user.save()
            return redirect('home_page1')


class UsersLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'auth/login_users.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password)
        if user:
            return render(request, 'home_view_2.html')
        else:
            return render(request, 'login_not_found.html')
