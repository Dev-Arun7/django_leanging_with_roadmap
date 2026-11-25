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

    # NEW: Database-level rules for Student
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(age__gte=5, age__lte=100),
                name="student_age_between_5_and_100"
            )
        ]

    def __str__(self):
        return self.name