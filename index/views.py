from django.shortcuts import render
from course.models import Course
from django.shortcuts import redirect
from django.contrib.auth import logout as log

# Create your views here.
def index(r):
    return render(r, 'index.html', {'var': 'value'})

def course(r):
    courses = Course.objects.all()

    def f(lst, n):
        return [lst[i:i + n] for i in range(0, len(lst), n)]

    list_courses = f(courses, 3)

    return render(r, 'course.html', {'courses': list_courses})

def logout(r):
    log(r)
    return redirect('/')
