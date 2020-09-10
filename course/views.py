from django.shortcuts import render
from course.models import Course


# Create your views here.
def index(r):
    return render(r, 'course.html', {'var': 'courses'})
    #rep


def course_detail(r, slug):
    course = Course.objects.get(name_slug=slug)
    return render(r, 'course_detail.html', {'course': course})
