from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from .models import Teacher, Subject, Chapter, Student, PointOfContact, Classroom, ClassroomShape, Class
from .forms import TeacherSearchForm


def index(request):
    return render(request, 'classroomapp/index.html', {"index": True})


class TeacherSearch(TemplateView):
    form_class = TeacherSearchForm

    def get(self, request, *args, **kwargs):
        """handle get request here"""
        response = {"form": TeacherSearchForm(), "index": False, "page": "teacher_search"}
        return render(request, 'classroomapp/teacher_search.html', response)

    def post(self, request, *args, **kwargs):
        """handle post request here"""

        #context = {}
        form = TeacherSearchForm(request.POST)
        #context.update({'form': form})
        if form.is_valid():
            print(form.cleaned_data)
            teacher_name = form.cleaned_data["teacher"]
            teacher_list = form.make_search(teacher_name)

            response = {"form": form, "class": teacher_list, "index":False, "page":"teacher_search"}

            '''
            query = form.cleaned_data.get("teacher")
            classes = form.save(query=query)
            context.update({"class":classes})
            '''
        return render(request, 'classroomapp/teacher_search.html', response)


def class_preview(request):
    class_list = Class.manager.all()
    response = {"class_list": class_list, "index": False, "page": "preview"}
    print(response)
    return render(request, "classroomapp/class_preview.html", response)