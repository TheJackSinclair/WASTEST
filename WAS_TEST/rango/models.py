from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    heading = models.CharField(max_length=128, unique=True)
    date = models.CharField(max_length=128, unique=True)
    body = models.CharField(max_length=50000, unique=True)
    def __str__(self):
        return self.heading