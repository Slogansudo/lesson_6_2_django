from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def users_views(request):
    return HttpResponse("""
            <h1>This is users page can I help you<h1>
            <div>
            <a href='http://127.0.0.1:8000/students/' target='_blank'>info_about_students</a>
            </div>
            <a href='http://127.0.0.1:8000/mentors/' target='_blank'>info_about_mentors</a>
            """)


def students_views(request):
    return render(request, 'users_data1.html')
