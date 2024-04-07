from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Students


# Create your views here.


class StudentsView(View):
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
