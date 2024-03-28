from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.IntegerField()
    description = models.TextField()

