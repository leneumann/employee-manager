from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name