
from django.db import models
from django.conf import settings 


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)

    image = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    document = models.FileField(
        upload_to="student_documents/",
        blank=True,
        null=True
    )

    courses = models.ManyToManyField(
        "courses.Course",
        blank=True,
        related_name="enrolled_students"
    )

    # Database-level rules for student
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(age__gte=5, age__lte=100),
                name="student_age_between_5_and_100"
            )
        ]

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.student.name}'s profile"


# Staff profile extend django's built in User model
class StaffProfile(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ("prefer_not_to_say", "Prefer not to say"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="staff_profile"
    )

    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True
    )

    image = models.ImageField(
        upload_to="staff/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
