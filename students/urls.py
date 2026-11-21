from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.student_list, name="student_list"),
    path("<int:student_id>/", views.student_detail, name="student_detail"),
    path("about/", views.about, name="about"),
    path("add/", views.add_student, name="add_student"),
    path("edit/<int:student_id>/", views.edit_student, name="edit_student"),
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
    path("age/<int:age>/", views.student_by_age, name="student_by_age"),
    path("name/<str:name>/", views.student_by_name, name="student_by_name"),
    path("search/<slug:name>/", views.student_by_slug, name="student_by_slug"),
    path("login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("account/", views.account_profile, name="account_profile"),
    path("register/", views.register, name="register"),
    path("password-change/", 
        auth_views.PasswordChangeView.as_view(template_name="students/password_change.html", 
        success_url=reverse_lazy("account_profile")), 
        name="password_change"),
    # Password reset through backend emil
    # Step 1: Enter email address
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="students/password_reset.html",
            email_template_name="students/password_reset_email.txt",
            subject_template_name="students/password_reset_subject.txt",
            success_url=reverse_lazy("password_reset_done")
        ),
        name="password_reset"
    ),

    # Step 2: Email sent confirmation
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="students/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    # Step 3: Open the reset link and enter a new password
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="students/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset_complete")
        ),
        name="password_reset_confirm"
    ),

    # Step 4: Password successfully changed
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="students/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
    path("session-demo/", views.session_demo, name="session_demo"),
    path("cookie-demo/", views.cookie_demo, name="cookie_demo"),
    ]