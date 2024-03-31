from django.db import models


class UserStudents(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
