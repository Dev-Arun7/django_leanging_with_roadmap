from django.test import TestCase
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.urls import reverse, resolve


class StudentModelTest(TestCase):

    def test_create_student(self):
        student = Student.objects.create(
            name="Arun",
            age=25,
            email="arun@example.com"
        )

        self.assertEqual(student.name, "Arun")
        self.assertEqual(student.age, 25)
        self.assertEqual(student.email, "arun@example.com")

    def test_student_string(self):
        student = Student.objects.create(
            name="Rahul",
            age=28,
            email="rahul@example.com"
        )

        self.assertEqual(str(student), "Rahul")


class StudentListViewTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name="Test Student",
            age=25,
            email="test@example.com"
        )

    def test_student_list_status_code(self):
        response = self.client.get(reverse("student_list"))

        self.assertEqual(response.status_code, 200)

    def test_student_list_template(self):
        response = self.client.get(reverse("student_list"))

        self.assertTemplateUsed(response, "students/student_list.html")

    def test_student_list_contains_student(self):
        response = self.client.get(reverse("student_list"))

        self.assertContains(response, "Test Student")


class StudentFormTest(TestCase):

    def test_valid_student_form(self):
        form_data = {
            "name": "Arun",
            "age": 25,
            "email": "arun@example.com",
        }

        form = StudentForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_invalid_age(self):
        form_data = {
            "name": "Arun",
            "age": 5,
            "email": "arun@example.com",
        }

        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())


    def test_age_above_limit(self):
        form_data = {
            "name": "Arun",
            "age": 90,
            "email": "arun@example.com",
        }

        form = StudentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            "name": "Arun",
            "age": 25,
            "email": "invalid-email",
        }

        form = StudentForm(data=form_data)

        self.assertFalse(form.is_valid())


class StudentURLTest(TestCase):

    def test_student_list_url_resolves(self):
        url = reverse("student_list")
        view = resolve(url)

        self.assertEqual(view.view_name, "student_list")

    def test_student_list_url_returns_200(self):
        url = reverse("student_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_unknown_url_returns_404(self):
        response = self.client.get("/this-url-does-not-exist/")

        self.assertEqual(response.status_code, 404)