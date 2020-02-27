from django.urls import path

from . import views

app_name= 'classroomapp'

urlpatterns = [
    path('',views.index, name='index'),
    path("class_preview", views.class_preview, name="class_preview"),
]