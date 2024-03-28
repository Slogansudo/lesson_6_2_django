from django.urls import path
from .views import users_views, students_views
from .views2 import mentor_views

urlpatterns = [
    path('users/', users_views),
    path('students/', students_views),
    path('mentors/', mentor_views)
]
