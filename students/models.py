from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)

    courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        related_name="enrolled_students"
    )

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student=models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15, blank=True)
    address=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.student.name}'s profile"