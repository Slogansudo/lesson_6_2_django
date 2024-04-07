from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Books, BookAuthor, StudentsBook
from users.models import Students


class LibraryView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            books = Books.objects.all()
            return render(request, "library_home.html", {"books": books})
        else:
            books = Books.objects.filter(title__icontains=search)
            return render(request, "library_home.html", {"books": books, 'search': search})


class BooksView(View):
    def get(self, request, id):
        book = Books.objects.get(id=id)
        return render(request, 'book_data.html', {'book': book, 'search':search})


class StudentsBookView(View):
    def get(self, request):
        s_books = StudentsBook.objects.all()
        return render(request, 'students_book.html', {'students_book': s_books})


