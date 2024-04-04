from django.db import models
from users.models import Students


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Comments(models.Model):
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"


class Books(models.Model):
    title = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    description = models.TextField()
    create_date = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.title} {self.year}"


class BookAuthor(models.Model):
    book = models.ManyToManyField(Books)
    author = models.ManyToManyField(Author)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book} {self.author}"


class StudentsBook(models.Model):
    student = models.ManyToManyField(Students)
    books = models.ManyToManyField(Books)
    comments = models.ManyToManyField(Comments, null=True, blank=True)
    take_date = models.DateTimeField(auto_now_add=True)
    returned_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.books} {self.returned_status}"








