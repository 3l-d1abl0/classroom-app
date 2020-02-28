from django import forms
from .models import Class, Subject
from django.db.models import Sum, Count

class TeacherSearchForm(forms.Form):
    """Form to search teacher"""

    teacher = forms.CharField(label='Teacher', max_length=30)
    teacher.widget.attrs.update({'class': 'form-control'})
    teacher.widget.attrs.update({'required': True})
    teacher.widget.attrs.update({'placeholder': 'Type teacher\'s Name'})

    def make_search(self, teacher_name):
        teacher_list = Class.manager.filter_by_teachers(teacher_name)
        print(teacher_list)
        return teacher_list

class SubjectSearchForm(forms.Form):
    """Form to search Subject"""

    subject = forms.ModelChoiceField(empty_label="Select a Subject", queryset=Subject.objects.all())
    subject.widget.attrs.update({'class': 'form-control'})

    def make_search(self, query):
        subject = Class.manager.filter(subject=query)
        teachers = subject.aggregate(Count("teacher", distinct=True))
        students = subject.aggregate(Count("students", distinct=True))
        total_hours = subject.aggregate(Sum("subject__total_duration"))
        #print(total_hours)
        return {"teachers":teachers, "students":students, "total_hours":total_hours}