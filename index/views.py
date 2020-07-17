from django.shortcuts import render

# Create your views here.
def index(r):
    return render(r, 'index.html', {'var': 'value'})

def course(r):
    return render(r, 'course.html', {'var': 'value'})
