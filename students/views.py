from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages  


# Create your views here.
def home(request):
    students = Student.objects.all()
    data = {"students":students}
    return render(request, "students/home.html", data)

def student_list(request):
    students = Student.objects.all()

    return render(request, "students/student_list.html", {
        "students": students
    })

# Profile page
@login_required
def account_profile(request):
    return render(request, "students/account_profile.html", {
        "user": request.user
    })


# Student Profile
@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    # A student may not have a StudentProfile yet.
    profile = getattr(student, "studentprofile", None)

    return render(request, "students/student_detail.html", {
        "student": student,
        "profile": profile,
    })


def about(request):
    return render(request, 'students/about.html')


@staff_member_required
@permission_required("students.add_student", raise_exception=True)
def add_student(request):
    if  request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            # Create message
            messages.success(request, "Student added successfully!")

            # Reverse used to generate url 
            url = reverse("student_list")
            return redirect(url)
        else:
            print(form.errors)
    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {"form": form})


@staff_member_required
@permission_required("students.change_student", raise_exception=True)
def edit_student(request, student_id):
    # Get the student using the ID
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        # Fill the form with submitted data and the existing student
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect("student_detail", student_id=student.id)

    else:
        # Display the form with existing student details
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {
        "form": form,
        "student": student
    })


@staff_member_required
@permission_required("students.delete_student", raise_exception=True)
def delete_student(request, student_id):
    # Get the student or 404 if not exist
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully!")
        messages.error(request, "This is an error message!")
        messages.warning(request, "This is a warning message!")
        messages.info(request, "This is an information message!")
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {
        "student":student
    })


@login_required
def student_by_age(request, age):
    students = Student.objects.filter(age=age)
    return render(request, "students/student_list.html",{
        "students":students
    })


@login_required
def student_by_name(request, name):
    students = Student.objects.filter(name__iexact=name)
    return render(request, "students/student_list.html",{
        "students":students
    })


@login_required
# Slug using to pass alpha numericals eg: search keyword (special symbols not accept here)
def student_by_slug(request, name):
    # Convert student name
    student_name = name.replace("-", " ")
    students = Student.objects.filter(name__iexact=student_name)
    return render(request, "students/student_list.html", {
        "students":students
    })


# User registration
def register(request):

    if request.method == "POST":

        # Get the submitted registration data
        form = UserCreationForm(request.POST)

        if form.is_valid():

            # Create the new user
            form.save()

            # Redirect to login page
            return redirect("login")

    else:

        # Display an empty registration form
        form = UserCreationForm()

    return render(request, "students/register.html", {
        "form": form
    })



def session_demo(request):
    request.session.set_expiry(3)

    if request.method == "POST":
        request.session.pop("visit_count", None)

        # Show zero immediately after resetting
        return render(request, "students/session_demo.html", {
            "visit_count": 0
        })

    visit_count = request.session.get("visit_count", 0)

    visit_count += 1

    if visit_count > 10:
        request.session["visit_count"] = 0
    else:
        request.session["visit_count"] = visit_count

    request.session["username"] = "Arun_from_session"
    session_name = request.session.get("username")
    

    return render(request, "students/session_demo.html", {
        "visit_count": visit_count,
        "session_name": session_name
    })


def cookie_demo(request):

    # Read the existing cookie
    theme = request.COOKIES.get("theme", "light")

    if request.method == "POST":

        action = request.POST.get("action")

        # Delete the cookie
        if action == "delete":

            response = render(request, "students/cookie_demo.html", {
                "theme": "light",
                "message": "Theme preference removed!"
            })

            response.delete_cookie("theme")

            return response

        # Save the selected theme
        theme = request.POST.get("theme", "light")

        response = render(request, "students/cookie_demo.html", {
            "theme": theme,
            "message": "Theme preference saved!"
        })

        # Cookie will last for 30 days
        response.set_cookie(
            "theme",
            theme,
            max_age=60 * 60 * 24 * 30,
            httponly=True,
            samesite="Lax"
        )

        return response

    return render(request, "students/cookie_demo.html", {
        "theme": theme
    })