from django.shortcuts import render

# Create your views here.

from .models import Teacher, Subject, Chapter, Student, PointOfContact, Classroom, ClassroomShape, Class


def index(request):
    return render(request, 'classroomapp/index.html')