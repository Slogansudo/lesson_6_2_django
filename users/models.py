from django.db import models


class UserStudents(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    address_name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address_name}"



