from django.db import models


class Address(models.Model):
    address_name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.address_name}"


class Level(models.TextChoices):
    b = ("b", "B")
    m = ('m', "M")
    p = ('ph', "PH")


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=Level.choices, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    password = models.TextField()
    image = models.ImageField(upload_to='media/Students')
    last_update = models.DateTimeField(auto_now=True)

    class Mode:
        db_table = 'students_user'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
