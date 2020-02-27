from django.shortcuts import render

# Create your views here.

from .models import Teacher, Subject, Chapter, Student, PointOfContact, Classroom, ClassroomShape, Class


def index(request):
    return render(request, 'classroomapp/index.html', {"index": True})



def class_preview(request):
    class_list = Class.objects.all()
    response = {"class_list": class_list, "index": False, "page": "preview"}
    print(response)
    return render(request, "classroomapp/class_preview.html", response)