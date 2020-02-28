from django.shortcuts import render
from django.views.generic import TemplateView

from django.db.models import Sum, Count

# Create your views here.

from .models import Teacher, Subject, Chapter, Student, PointOfContact, Classroom, ClassroomShape, Class
from .forms import TeacherSearchForm, SubjectSearchForm


def index(request):
    return render(request, 'classroomapp/index.html', {"index": True})

#4
class SubjectSearch(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'classroomapp/subject_search.html', {'form': SubjectSearchForm(), "index": False, "page": "subject_search"})

    def post(self, request, *args, **kwargs):

        form = SubjectSearchForm(request.POST)
        response ={'form': form, "index": False, "page": "subject_search"}

        if form.is_valid():
            subject_name = form.cleaned_data["subject"]
            data = form.make_search(subject_name)
            response.update(data)

        return render(request, 'classroomapp/subject_search.html', response)


#3
def teacher_search_by_salary(request):

    salary_limit = 100000
    classes =  Class.manager.filter(teacher__salary__gt=salary_limit)
    
    sum_teachers = classes.aggregate(Count("teacher", distinct=True))
    sum_students = classes.aggregate(Count("students", distinct=True))
    sum_salaries = classes.aggregate(Sum("teacher__salary"))
    
    response = { "teachers": sum_teachers, "students": sum_students, "salaries":sum_salaries,
                  "index": False, "page": "teacher_search_by_salary"}
    return render(request, "classroomapp/teacher_search_by_salary.html", response)

#2
class TeacherSearch(TemplateView):
    form_class = TeacherSearchForm

    def get(self, request, *args, **kwargs):
        """handle get request here"""
        response = {"form": TeacherSearchForm(), "index": False, "page": "teacher_search"}
        return render(request, 'classroomapp/teacher_search.html', response)

    def post(self, request, *args, **kwargs):
        """handle post request here"""

        form = TeacherSearchForm(request.POST)
        response = {"form": form, "index":False, "page":"teacher_search"}

        if form.is_valid():
            teacher_name = form.cleaned_data["teacher"]
            teacher_list = form.make_search(teacher_name)
            response.update({"class": teacher_list})

        return render(request, 'classroomapp/teacher_search.html', response)

#1
def class_preview(request):
    class_list = Class.manager.all()
    response = {"class_list": class_list, "index": False, "page": "preview"}
    return render(request, "classroomapp/class_preview.html", response)