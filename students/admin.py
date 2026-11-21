from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "age", "email", "date_joined")
    list_filter = ("age", "date_joined")
    search_fields = ("name", "email")
    ordering = ("age",)
    