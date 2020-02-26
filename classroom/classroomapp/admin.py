from django.contrib import admin

from .models import Teacher, Subject, Chapter, Student, PointOfContact, Classroom, ClassroomShape, Class


admin.site.site_header = "Classroom Admin"
admin.site.site_title = "Admin area"
admin.site.index_title = "Welcom to Admin area"

# Register your models here.
 

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Student)
admin.site.register(PointOfContact)
admin.site.register(Classroom)
admin.site.register(ClassroomShape)
admin.site.register(Class)