from django.urls import path
from .views import StudentsView, StudentDetailView

urlpatterns = [
    path('students/', StudentsView.as_view(), name='students'),
    path('students/<int:id>/', StudentDetailView.as_view(), name='students_date')
]
