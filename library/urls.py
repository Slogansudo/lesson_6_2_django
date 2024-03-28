from django.urls import path
from .views import library_view, choose_language
from .view2 import library_view2

urlpatterns = [
    path('library/', choose_language),
    path('uzb/', library_view),
    path('english/', library_view2)
]
