from django.contrib import admin
from .models import Author, Books, BookAuthor, StudentsBook, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_display_links = ('id', 'first_name', 'last_name', 'birth_date')
    search_fields = ('id', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name', )
    ordering = ('id', 'first_name')


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'year', 'description', 'create_date')
    list_display_links = ('id', 'title', 'year', 'description', 'create_date')
    search_fields = ('id', 'title', 'year',)
    list_filter = ('id', 'title')
    ordering = ('id', 'title')


@admin.register(BookAuthor)
class BooksAuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'create_date')
    list_display_links = ('id', 'create_date')
    search_fields = ('id', )
    list_filter = ('id', )
    ordering = ('id',)


@admin.register(StudentsBook)
class StudentsBookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'take_date', 'returned_status')
    list_display_links = ('id', 'take_date', 'returned_status')
    search_fields = ('id', )
    list_filter = ('id', )
    ordering = ('id', )


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comment', 'create_date')
    list_display_links = ('id', 'comment', 'create_date')
    search_fields = ('id', )
    list_filter = ('id', )
    ordering = ('id', )

