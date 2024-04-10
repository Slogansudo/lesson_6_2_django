from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import Students
from django.contrib.auth.models import User
from .forms import StudentsLoginForm, StudentsRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class StudentsView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            students = Students.objects.all()
            return render(request, "students_home.html", {"students": students})
        else:
            students = Students.objects.filter(first_name__icontains=search)
            return render(request, "students_home.html", {"students": students, 'search': search})


class StudentDetailView(View):
    def get(self, request, id):
        students_date = Students.objects.get(id=id)
        return render(request, 'students_date.html', {'students_date': students_date})


class StudentsRegisterView(View):
    def get(self, request):
        forms = StudentsRegisterForm()
        return render(request, 'auth/register_students.html', {'forms': forms})

    def post(self, request):
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        status = data['status']
        password_1 = data['password_1']
        password_2 = data['password_2']
        if password_2 == password_1:
            student = Students(first_name=first_name, last_name=last_name, username=username, email=email, status=status, password=password_1)
            student.save()
            return redirect('home_page1')
        else:
            return redirect('register_s')


class StudentsLoginView(View):
    def get(self, request):
        form = StudentsLoginForm()
        return render(request, 'auth/login_students.html', {'forms': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        student = Students.objects.filter(username=username, password=password).first()
        if student:
            return redirect('home_page1')
        else:
            return render(request, 'login_not_found.html')
