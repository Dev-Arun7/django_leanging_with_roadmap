from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'name': 'Arun',
        'age': 33,
        'course': 'Django',
        'students':["arun", "akhil", "anu", "simba"]
    }
    return render(request, "students/home.html", data)


def about(request):
    return render(request, 'students/about.html')