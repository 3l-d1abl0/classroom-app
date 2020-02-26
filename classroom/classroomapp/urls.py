from django.urls import path

from . import views

app_name= 'classroomapp'

urlpatterns = [
    path('',views.index, name='index')
]