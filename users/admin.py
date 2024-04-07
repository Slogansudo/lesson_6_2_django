from django.contrib import admin
from .models import Students, Address
from import_export.admin import ImportExportModelAdmin


@admin.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'age', 'status', 'address', "last_update")
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'age', 'status', 'address', "last_update")
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('first_name', 'address')
    autocomplete_fields = ('address', )


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'address_name', 'create_date')
    list_display_links = ('id', 'address_name')
    search_fields = ('id', 'address_name')
    ordering = ('id', 'address_name')



