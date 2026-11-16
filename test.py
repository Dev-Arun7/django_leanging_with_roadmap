from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name