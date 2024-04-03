from django.contrib import admin
from .models import Author, Books, BookAuthor, StudentsBook, Comments

admin.site.register(Author)
admin.site.register(Books)
admin.site.register(BookAuthor)
admin.site.register(StudentsBook)
admin.site.register(Comments)

