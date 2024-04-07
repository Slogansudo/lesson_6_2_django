from django.urls import path
from .views import LibraryView, BooksView, StudentsBookView
urlpatterns = [
    path("library/", LibraryView.as_view(), name="library"),
    path("library/<int:id>/", BooksView.as_view(), name="book_data"),
    path("library/students/", StudentsBookView.as_view(), name="students_book"),
]
