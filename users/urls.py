from django.urls import path
from .views import StudentsView, StudentDetailView, StudentsRegisterView, StudentsLoginView

urlpatterns = [
    path('students/', StudentsView.as_view(), name='students'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='students_date'),
    path('register/students/', StudentsRegisterView.as_view(), name='register_s'),
    path('login/students', StudentsLoginView.as_view(), name='login_s')
]
