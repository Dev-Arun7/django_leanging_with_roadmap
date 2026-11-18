from django.db import migrations


def copy_courses(apps, schema_editor):
    Student = apps.get_model("students", "Student")
    Course = apps.get_model("courses", "Course")

    for student in Student.objects.all():
        if student.course_id:
            course = Course.objects.get(pk=student.course_id)
            student.courses.add(course)


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0006_student_courses"),
    ]

    operations = [
        migrations.RunPython(
            copy_courses,
            migrations.RunPython.noop
        ),
    ]