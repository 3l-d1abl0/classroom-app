from django.urls import path

from . import views

app_name= 'classroomapp'

urlpatterns = [
    path('',views.index, name='index'),
    path("class_preview", views.class_preview, name="class_preview"),
    path("teacher_search", views.TeacherSearch.as_view(), name="teacher_search"),
    path("teacher_search_by_salary", views.teacher_search_by_salary, name="teacher_search_by_salary"),
    path("subject_search", views.SubjectSearch.as_view(), name="subject_search"),
]