
def session_demo(request):

    # If the user clicks the reset button
    if request.method == "POST":
        request.session.pop("visit_count", None)
        return redirect("session_demo")

    # Get the current count from the session
    visit_count = request.session.get("visit_count", 0)

    # Increase the count
    visit_count += 1

    # Save the updated count in the session
    request.session["visit_count"] = visit_count

    return render(request, "students/session_demo.html", {
        "visit_count": visit_count
    })
