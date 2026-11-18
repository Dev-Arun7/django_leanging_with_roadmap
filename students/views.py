from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

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


def about(request):
    return render(request, 'students/about.html')


def add_student(request):
    if  request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {"form": form})


def edit_student(request, student_id):
    # Get the student using the ID
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        # Fill the form with submitted data and the existing student
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")

    else:
        # Display the form with existing student details
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {
        "form": form,
        "student": student
    })


def delete_student(request, student_id):
    # Get the student or 404 if not exist
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "students/confirm_delete.html", {
        "student":student
    })