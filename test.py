def delete_student(request, student_id):
    # Get the student. Return 404 if the student does not exist.
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/confirm_delete.html", {
        "student": student
    })