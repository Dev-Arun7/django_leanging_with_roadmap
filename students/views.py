from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, UserAccountForm, StaffProfileForm
from .models import Student
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
# For calss based views
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth import get_user_model




User = get_user_model()



# Create your views here.
def home(request):
    return render(request, "students/home.html")


# def student_list(request):
#     students = Student.objects.all()

#     return render(request, "students/student_list.html", {
#         "students": students
#     })


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"


# Profile page
@login_required
def account_profile(request):
    return render(request, "students/account_profile.html", {
        "user": request.user
    })


# Student Profile
# @login_required
# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)

#     # A student may not have a StudentProfile yet.
#     profile = getattr(student, "studentprofile", None)

#     return render(request, "students/student_detail.html", {
#         "student": student,
#         "profile": profile,
#     })


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"
    pk_url_kwarg = "student_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the student's profile, if available
        context["profile"] = getattr(
            self.object,
            "studentprofile",
            None
        )

        return context




class AboutView(TemplateView):
    template_name = "students/about.html"


# @staff_member_required
# @permission_required("students.add_student", raise_exception=True)
# def add_student(request):
#     if  request.method == "POST":
#         form = StudentForm(request.POST)

#         if form.is_valid():
#             form.save()

#             # Create message
#             messages.success(request, "Student added successfully!")

#             # Reverse used to generate url 
#             url = reverse("student_list")
#             return redirect(url)
#         else:
#             print(form.errors)
#     else:
#         form = StudentForm()

#     return render(request, "students/add_student.html", {"form": form})


class AddStudentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
    CreateView
    ):
    model = Student
    form_class = StudentForm
    template_name = "students/add_student.html"
    success_url = reverse_lazy("student_list")

    permission_required = "students.add_student"
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Student added successfully!")
        return super().form_valid(form)


# @staff_member_required
# @permission_required("students.change_student", raise_exception=True)
# def edit_student(request, student_id):
#     # Get the student using the ID
#     student = get_object_or_404(Student, id=student_id)

#     if request.method == "POST":
#         # Fill the form with submitted data and the existing student
#         form = StudentForm(request.POST, instance=student)

#         if form.is_valid():
#             form.save()
#             messages.success(request, "Student updated successfully!")
#             return redirect("student_detail", student_id=student.id)

#     else:
#         # Display the form with existing student details
#         form = StudentForm(instance=student)

#     return render(request, "students/edit_student.html", {
#         "form": form,
#         "student": student
#     })


class EditStudentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
    UpdateView
    ):
    model = Student
    form_class = StudentForm
    template_name = "students/edit_student.html"
    context_object_name = "student"

    pk_url_kwarg = "student_id"

    permission_required = "students.change_student"
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return reverse(
            "student_detail",
            kwargs={"student_id": self.object.id}
        )

    def form_valid(self, form):
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)


# @staff_member_required
# @permission_required("students.delete_student", raise_exception=True)
# def delete_student(request, student_id):
#     # Get the student or 404 if not exist
#     student = get_object_or_404(Student, id=student_id)

#     if request.method == "POST":
#         student.delete()
#         messages.success(request, "Student deleted successfully!")
#         messages.error(request, "This is an error message!")
#         messages.warning(request, "This is a warning message!")
#         messages.info(request, "This is an information message!")
#         return redirect("student_list")
#     return render(request, "students/confirm_delete.html", {
#         "student":student
#     })


class DeleteStudentView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
    DeleteView
):
    model = Student
    template_name = "students/confirm_delete.html"
    context_object_name = "student"

    pk_url_kwarg = "student_id"

    permission_required = "students.delete_student"
    raise_exception = True

    success_url = reverse_lazy("student_list")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Student deleted successfully!")
        return super().form_valid(form)


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


class StaffListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "students/staff_list.html"
    context_object_name = "staff_list"
    ordering = ["username"]



@login_required
def account_profile(request):

    staff_profile = request.user.staff_profile

    # Check whether the user clicked Edit Profile
    edit_mode = request.GET.get("edit") == "true"

    if request.method == "POST":

        user_form = UserAccountForm(
            request.POST,
            instance=request.user
        )

        profile_form = StaffProfileForm(
            request.POST,
            request.FILES,
            instance=staff_profile
        )

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(request, "Your profile was updated successfully.")

            return redirect("account_profile")

        # If validation fails, keep the edit form visible
        edit_mode = True

    else:

        user_form = UserAccountForm(instance=request.user)
        profile_form = StaffProfileForm(instance=staff_profile)

    return render(
        request,
        "students/account_profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "user": request.user,
            "edit_mode": edit_mode,  # NEW
        }
    )


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "students/staff_detail.html"
    context_object_name = "staff"